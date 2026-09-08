from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

# from .options import HardMode

if TYPE_CHECKING:
    from .world import ClankWorld


def set_all_rules(world: ClankWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ClankWorld) -> None:
    pass


def set_all_location_rules(world: ClankWorld) -> None:
    # set the location specific rules
    
    # artifacts
    # get all starting artifacts
    options_starting_artifacts = world.options.starting_artifacts.value
    non_starting_artifacts = []
    for key, option_value in options_starting_artifacts.items():
        if option_value != 1:
            non_starting_artifacts.append(key)
    # add rules for all non-starting artifacts
    for i in non_starting_artifacts:
        world.set_rule(world.get_location(f"Artifact Extraction: {i}"), Has(f"Artifact Unlock: {i}"))
        print(i)
    print(non_starting_artifacts)

def set_completion_condition(world: ClankWorld) -> None:
        # get all starting artifacts
    options_starting_artifacts = world.options.starting_artifacts.value
    non_starting_artifacts = []
    for key, option_value in options_starting_artifacts.items():
        if option_value != 1:
            non_starting_artifacts.append(f"Artifact Unlock: {key}")
    # add completion rule
    world.set_completion_rule(HasAll(*non_starting_artifacts))