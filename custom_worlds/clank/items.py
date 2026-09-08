from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ClankWorld

# data imports
from .item_data import ITEM_NAME_TO_ID, DEFAULT_ITEM_CLASSIFICATIONS, ITEM_TYPES


class ClankItem(Item):
    game = "Clank!"


def get_random_filler_item_name(world: ClankWorld) -> str:
    #if world.random.randint(0, 99) < world.options.Filler_6_Chance:
    return "filler"


def create_item_with_correct_classification(world: ClankWorld, name: str) -> ClankItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return ClankItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    

def create_all_items(world: ClankWorld) -> None:

    # create the pool and items to add lists
    itempool: list[Item] = []
    ITEMS_TO_ADD = []


    # create all needed items

    # artifact unlocks
    # obtain starting artifacts
    options_starting_artifacts = world.options.starting_artifacts.value
    starting_artifacts = []
    for key, option_value in options_starting_artifacts.items():
        if option_value == 1:
            starting_artifacts.append(f"Artifact Unlock: {key}")

    # add all non-starting artifacts to the pool
    for i in ITEM_TYPES["artifact_unlock"]:
        if i not in starting_artifacts:
            ITEMS_TO_ADD.append(i)


    # insert all the items into the pool
    for i in ITEMS_TO_ADD:
        itempool.append(world.create_item(i))
        

    # get number of required filler items
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create the filler items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]


    # add items to the multiworld
    world.multiworld.itempool += itempool