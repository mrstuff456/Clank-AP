from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ClankWorld

# Import Data
from .location_data import LOCATION_NAME_TO_ID, LOCATION_TYPES


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ClankLocation(Location):
    game =  "Clank!"


# helper method that creates dictionary of all locations and their ID's
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ClankWorld) -> None:
    create_shop_locations(world)
    create_regular_locations(world)
    create_events(world)


def create_shop_locations(world: ClankWorld) -> None:
    # this function creates all the location names and IDs for the bonus row and bonus market
    amount_of_bonus_row = world.options.bonus_row_cards.value
    starting_id = LOCATION_NAME_TO_ID["end_of_dict"] + 1
    bonus_row_items = []
    for i in range(amount_of_bonus_row):
        LOCATION_NAME_TO_ID[f"Bonus Row Unlock {i + 1}"] = starting_id + i
        bonus_row_items.append(f"Bonus Row Unlock {i + 1}")
    LOCATION_TYPES["bonus_row"] = bonus_row_items
        

def create_regular_locations(world: ClankWorld) -> None:
    # put all locations into regions

    # grab all the regions as in regions.py
    overall_region = world.get_region("Overall Region")
    base_board = world.get_region("Base Front")
    advanced_board = world.get_region("Base Back")


    # assign locations to regions
    # seup region lists
    overall_region_locations = {}
    base_board_locations = {}
    advanced_board_locations = {}


    # locations setup

    # artifact extraction
    overall_region_locations.update(
        get_location_names_with_ids(LOCATION_TYPES["artifact_extraction"])
    )

    # gem collection checks
    if world.options.gem_collection:
        overall_region_locations.update(
            get_location_names_with_ids(LOCATION_TYPES["gem_collection"])
        )

    # rowsanity
    if world.options.rowsanity:
        overall_region_locations.update (
            get_location_names_with_ids(LOCATION_TYPES["rowsanity"])
        )

    # bonus row
    overall_region_locations.update(
        get_location_names_with_ids(LOCATION_TYPES["bonus_row"])
    )


    overall_region.add_locations(overall_region_locations, ClankLocation)
    base_board.add_locations(base_board_locations, ClankLocation)
    advanced_board.add_locations(advanced_board_locations, ClankLocation)


def create_events(world: ClankWorld) -> None:
    pass