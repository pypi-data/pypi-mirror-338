from corptools.models import EveItemType
from ninja import NinjaAPI, Schema

from django.db import transaction
from django.http import Http404

from allianceauth.eveonline.models import EveCharacter
from allianceauth.framework.api.user import get_all_characters_from_user
from allianceauth.services.hooks import get_extension_logger

from incursions.api.schema import CharacterSchema, HullSchema
from incursions.models.waitlist import (
    ActiveFleet, Fleet, FleetSquad, WaitlistCategory,
)
from incursions.providers import (
    get_characters_character_id_fleet, kick_all_fleet_members,
)


class FleetStatusFleetSchema(Schema):
    id: int
    boss: CharacterSchema


class FleetStatusResponse(Schema):
    fleets: list[FleetStatusFleetSchema] | None


class FleetInfoSquadSchema(Schema):
    id: int
    name: str


class FleetInfoWingSchema(Schema):
    id: int
    name: str
    squads: list[FleetInfoSquadSchema]


class FleetInfoResponse(Schema):
    fleet_id: int
    wings: list[FleetInfoWingSchema]


class FleetMemberSchema(Schema):
    id: int
    name: str | None = None
    ship: HullSchema
    role: str


class FleetCompSquadMembersSchema(Schema):
    id: int
    name: str
    members: list[FleetMemberSchema]


class FleetCompWingSchema(Schema):
    id: int
    name: str
    squads: list[FleetCompSquadMembersSchema]
    member: FleetMemberSchema | None = None


class FleetCompResponse(Schema):
    wings: list[FleetCompWingSchema] | None
    id: int | None
    member: FleetMemberSchema | None = None


class FleetMembersMemberSchema(Schema):
    id: int
    name: str | None = None
    ship: HullSchema
    wl_category: str | None = None
    category: str | None = None
    role: str


class FleetMembersResponse(Schema):
    members: list[FleetMembersMemberSchema]


class RegisterRequest(Schema):
    character_id: int
    fleet_id: int
    assignments: dict[str, tuple[int, int]]


logger = get_extension_logger(__name__)
api = NinjaAPI()


def setup(api: NinjaAPI) -> None:
    FleetAPIEndpoints(api)


class FleetAPIEndpoints:

    tags = ["Fleets"]

    def __init__(self, api: NinjaAPI) -> None:

        @api.get("/fleet/status", response={200: FleetStatusResponse, 403: dict}, tags=self.tags)
        def fleet_status(request):
            # Called regularly
            if not request.user.has_perm("incursions.basic_waitlist"):
                logger.warning(f"User {request.user} denied access to fleet status")
                return 403, {"error": "Permission denied"}

            try:
                active_fleet = ActiveFleet.get_solo()
                fleet = active_fleet.fleet
                if fleet is None:
                    raise ActiveFleet.DoesNotExist
                logger.info(f"User {request.user} retrieved active fleet {fleet.pk if fleet else None}")
                return 200, FleetStatusResponse(fleets=[fleet])
            except (ActiveFleet.DoesNotExist, Fleet.DoesNotExist):
                logger.info(f"No active fleet for user {request.user}")
                return 200, FleetStatusResponse(fleets=None)

        @api.get("/fleet/info", response={200: FleetInfoResponse, 403: dict}, tags=self.tags)
        def fleet_info(request, character_id: int):
            # Called only by Register, loads extra DB info to then register a fleet later
            if not request.user.has_perm("incursions.waitlist_manage_waitlist"):
                logger.warning(f"User {request.user} denied access to fleet info")
                return 403, {"error": "Permission denied"}

            esi_fleet = get_characters_character_id_fleet(character_id=character_id)

            if not esi_fleet:
                logger.error(f"Fleet not found for character {character_id}")
                raise Http404("Fleet not found")

            try:
                boss = EveCharacter.objects.get(character_id=character_id)
            except EveCharacter.DoesNotExist:
                boss = EveCharacter.objects.character_id(character_id=character_id)

            fleet = Fleet.objects.get_or_create(pk=esi_fleet.get("fleet_id"), boss=boss)[0]

            fleet_wings = fleet.get_fleets_fleet_id_wings()
            wings = [
                FleetInfoWingSchema(
                    id=wing.get("id"),
                    name=wing.get("name"),
                    squads=[FleetInfoSquadSchema(id=s.get("id"), name=s.get("name")) for s in wing.get("squads", [])],
                )
                for wing in fleet_wings
            ]
            logger.info(f"Fleet info fetched for fleet {fleet.pk} by user {request.user}")
            return FleetInfoResponse(fleet_id=fleet.pk, wings=wings)

        @api.get("/fleetcomp", response=FleetCompResponse, tags=self.tags)
        def fleet_composition(request, boss_character_id: int):
            if not request.user.has_perm("incursions.waitlist_fleet_view"):
                logger.warning(f"User {request.user} denied access to fleet composition")
                return 403, {"error": "Permission denied"}

            try:
                active_fleet = ActiveFleet.get_solo()
                fleet = active_fleet.fleet
                if fleet is None:
                    raise ActiveFleet.DoesNotExist
                logger.info(f"User {request.user} retrieved active fleet {fleet.pk if fleet else None}")
            except (ActiveFleet.DoesNotExist, Fleet.DoesNotExist):
                logger.info(f"No active fleet for user {request.user}")

            fleet_members = fleet.get_fleet_members()
            fleet_wings = fleet.get_fleets_fleet_id_wings()
            wings: list[FleetCompWingSchema] = []

            for wing in fleet_wings:
                squads: list[FleetMemberSchema] = []
                for fm in fleet_members:
                    if fm.get("wing_id") == wing.get("id"):
                        try:
                            character = EveCharacter.objects.only("character_name").get(pk=fm.get("character_id"))
                            ship = EveItemType.objects.only("name").get(pk=fm.get("ship_type_id"))
                        except (EveCharacter.DoesNotExist, EveItemType.DoesNotExist):
                            continue
                        squads.append(FleetMemberSchema(
                            id=fm.get("character_id"),
                            name=character.character_name,
                            ship=HullSchema(id=ship.pk, name=ship.name),
                            role=fm.get("role_name"),
                        ))
                wings.append(FleetCompWingSchema(id=wing.get("id"), name=wing.get("name"), squads=squads))

            logger.info(f"Fleet composition fetched for fleet {fleet.pk} by user {request.user}")
            return FleetCompResponse(wings=wings, id=fleet.pk)

        @api.get("/fleet/members/{character_id}", response=FleetMembersResponse, tags=self.tags)
        def fleet_members(request, character_id: int):
            if not request.user.has_perm("incursions.waitlist_fleet_view"):
                logger.warning(f"User {request.user} denied access to fleet members for character {character_id}")
                return 403, {"error": "Permission denied"}

            try:
                fleet = Fleet.objects.select_related("boss").get(boss__character_id=character_id)
            except Fleet.DoesNotExist:
                logger.error(f"Fleet not found for character {character_id}")
                raise Http404("Fleet not found")

            fleet_members = fleet.get_fleet_members()
            wings = {w.get("id"): w.get("name") for w in fleet.get_fleets_fleet_id_wings()}
            members: list[FleetMembersMemberSchema] = []

            for fm in fleet_members:
                try:
                    char = EveCharacter.objects.only("character_name").get(pk=fm.get("character_id"))
                    ship = EveItemType.objects.only("name").get(pk=fm.get("ship_type_id"))
                    squad = FleetSquad.objects.only("category").get(squad_id=fm.get("squad_id"))
                except (EveCharacter.DoesNotExist, EveItemType.DoesNotExist, FleetSquad.DoesNotExist):
                    continue

                members.append(FleetMembersMemberSchema(
                    id=fm.get("character_id"),
                    name=char.character_name,
                    ship=HullSchema(id=ship.pk, name=ship.name),
                    wl_category=squad.category.name,
                    category=f"{wings.get(fm.get('wing_id'))} - {fm.get('squad_name')}",
                    role=fm.get("role_name"),
                ))

            logger.info(f"Fleet members listed for fleet {fleet.pk} by user {request.user}")
            return FleetMembersResponse(members=members)

        @api.post("/fleet/register", tags=self.tags)
        def register_fleet(request, body: RegisterRequest):
            if not request.user.has_perm("incursions.waitlist_manage_waitlist"):
                logger.warning(f"User {request.user} denied fleet registration")
                return 403, {"error": "Permission denied"}

            # ARIEL check if request.body.character_id is owned by request.user
            # Recheck this
            if EveCharacter.objects.get(character_id=body.character_id) not in get_all_characters_from_user(request.user):
                logger.warning(f"User {request.user} attempted to register fleet with different character ID")
                return 403, {"error": "Permission denied"}

            with transaction.atomic():
                fleet, _ = Fleet.objects.select_for_update().get_or_create(
                    pk=body.fleet_id,
                    defaults={"boss": EveCharacter.objects.get(character_id=body.character_id)},
                )

                active_fleet = ActiveFleet.get_solo()
                active_fleet.fleet = fleet
                active_fleet.save(update_fields=["fleet"])

                for category, (wing_id, squad_id) in body.assignments.items():
                    cat = WaitlistCategory.objects.get(pk=category)
                    FleetSquad.objects.update_or_create(
                        fleet=fleet,
                        category=cat,
                        defaults={"wing_id": wing_id, "squad_id": squad_id},
                    )

            logger.info(f"Fleet {fleet.pk} registered and squads assigned by user {request.user}")
            return "OK"

        @api.post("/fleet/close", tags=self.tags)
        def close_fleet(request, boss_character_id: int):
            if not request.user.has_perm("incursions.waitlist_manage_waitlist"):
                logger.warning(f"User {request.user} denied closing fleet")
                return 403, {"error": "Permission denied"}

            fleet = ActiveFleet.get_solo().fleet
            count = kick_all_fleet_members(boss_character_id=fleet.boss.character_id, fleet_id=fleet.pk)
            logger.info(f"User {request.user} closed fleet {fleet.pk} and kicked {count} members")
            return f"Kicked {count} Fleet Members"
