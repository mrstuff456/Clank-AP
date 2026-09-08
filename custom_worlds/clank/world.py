from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world, components
from . import options as clank_options  # rename due to a name conflict with World.options


class ClankWorld(World):
    """
    Clank!AP is a manual archipelago implementation of Clank! A deckbuilding adventure.
    This is to be played with a physical copy of Clank! Expansions are optional.
    """

    game = "Clank!"

    web = web_world.ClankWebWorld()

    options_dataclass = clank_options.ClankOptions
    options: clank_options.ClankOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Overall Region"


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)


    def set_rules(self) -> None:
        rules.set_all_rules(self)


    def create_items(self) -> None:
        items.create_all_items(self)


    def create_item(self, name: str) -> items.ClankItem:
        return items.create_item_with_correct_classification(self, name)


    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)


    def fill_slot_data(self) -> Mapping[str, Any]:
        return {"wow": True}