from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ClankWorld


def create_and_connect_regions(world: ClankWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


# create all the regions needed
def create_all_regions(world: ClankWorld) -> None:
    # BASE <name> = Region("<name>", world.player, world.multiworld)

    # default regions
    overall_region = Region("Overall Region", world.player, world.multiworld)
    base_board = Region("Base Front", world.player, world.multiworld)
    advanced_board = Region("Base Back", world.player, world.multiworld)

    # add all the regions into a list
    regions = [overall_region, base_board, advanced_board]



    # add all the regions into the multiworld
    world.multiworld.regions += regions


def connect_regions(world: ClankWorld) -> None:
    # # get/define the regions
    overall_region = world.get_region("Overall Region")
    base_board = world.get_region("Base Front")
    advanced_board = world.get_region("Base Back")


    # connect the regions
    overall_region.connect(base_board, "Overall to Base Region")
    overall_region.connect(advanced_board, "Overall to Advanced Region")

    