from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionDict


# WOOOO DEATHLINK YAYAYAYAYA
class DeathLink(Toggle):
    """
    Because who doesnt love restarting runs
    A death in Clank! is losing all of your health
    When you receive a death, end your current run
    Default: False
    """


# Artifact Options
class Artifacts(Toggle):
    """
    Shuffle Artifacts to be unlocked into the multiworld
    (Bracelet and Ankh are not shuffled and used as starting Artifacts (for now))
    Default: True
    """
    display_name = "Artifacts"

    default = True


class StartingArtifacts(OptionDict):
    """
    What artifacts are given to you at the start, the rest are shuffled into the multiworld
    - 0 to disable, 1 to enable:
    """
    display_name = "Starting Artifacts"
    default = {
        "Bracelet": 1,
        "Ankh": 1,
        "Urn": 0,
        "Golden Banana": 0,
        "Shield": 0,
        "Chestplate": 0,
        "Golden Treasure": 0,
    }


# Monkey idol options
class MonkeyIdols(Toggle):
    """
    Wether Monkey Idols are shuffled into the Multiworld.
    Default: True
    """
    display_name = "Monkey Idols"

    default = True


class MonkeyIdolItemBehaviour(Choice):
    """
    Controls the Behaviour of how unlock checks are generated:
    - Individual (Reccomended): Unlocks all idols of a type (See, Speak, Hear).
    - AllIdols: One check which unlocks all idols at once.
    - PerBoardIndividual: Each Idol has its own check (See, Speak, Hear for each board).
    - PerBoardAll: Each board has one check which unlocks it's respective Idols.
    Default: Individual
    """
    display_name = "Idol Item Behaviour"

    option_Individual = 0
    option_AllIdols = 1
    option_PerBoardIndividual = 2
    option_PerBoardAll = 3
    default = 0


class MonkeyIdolLocationBehaviour(Toggle):
    """
    If True, Monkey idol collection checks are made for each board.
    If False, checks are cumulative for all boards (See, Speak, Hear).
    Default: True (Reccomended)
    """
    display_name = "Idol Checks Per Board"

    default = True


# Dungeon row options
class DungeonRow(Toggle):
    """
    Wether cards in the dungeon row are shuffled into the multiworld.
    - Don't disable this please you'll just kill 90% of the archipelago
    - Abandon all hope ye who enter here and such
    - Who am I to stop you though if you wanna be insane go ahead
    Default: True (as it should be)
    """
    display_name = "Dungeon Row"

    default = True


class RowShufflingStyle(Choice):
    """
    The style in which dungeon row cards are shuffled into the multiworld:
    - Packs (Reccomended): Cards are made into prebuilt "packs", each check unlocks a set of cards.
    - SmallPacks: Tighter groups for more checks.
    - RandomPacks: Like packs, but instead the card packs are randomly made on generation.
    - ProgressivePacks: cards are grouped by power, and each progressive check unlocks the next more powerful pack.
    - All: Each individual card must be unlocked via a check, not for the feint of heart!
    Default: Packs
    Requires DungeonRow to be True
    """
    display_name = "Row Shuffling Style"

    option_Packs = 0
    option_SmallPacks = 1
    option_RandomPacks = 2
    option_ProgressivePacks = 3
    option_All = 4
    default = 0


class PackSize(Range):
    """
    If using the RandomPacks or ProgressivePacks option, decides how big the size of the packs are.
    Default: 4
    """
    display_name = "Pack Size"

    range_start = 2
    range_end = 70
    default = 4


class RowSanity(Choice):
    """
    Locations for buying cards:
    - None: Disables RowSanity.
    - Gems: Each unique Gem card purchase is also a check.
    - All: Every card is a check (Reccomended for RowShufflingStyle = All).
    Default: Gems
    """
    display_name = "RowSanity"

    option_None = 0
    option_Gems = 1
    option_All = 2
    default = 1

# Bonus dungeon row options
class BonusRow(Toggle):
    """
    Weather locations are made for an extra shop that skill can be spent on.
    Please dont turn this off unless you have a REALLY good reason, this game needs locations </3
    Default: True
    """
    display_name = "Bonus Row"

    default = True


class BonusRowCards(Range):
    """
    The amount of cards you want to have in the Bonus Row
    - A majority of locations come from here, generally please do not decrease this number
    """
    display_name = "Bonus Row Cards"

    range_start = 30
    range_end = 100
    default = 50


class BonusRowPrices(OptionDict):
    """
    The cost of Bonus Row items depending on their type:
    """
    display_name = "Bonus Row Prices"
    default = {
        "progression": 5,
        "useful": 4,
        "filler": 3,
        "trap": 2,
        "junk": 2,
    }


# # Expansion options
# class MummysCurse(Toggle):
#     """
#     Wether to include the Mummy's Curse DLC content:
#     - This includes both boards and all the extras included in the expansion
#     Default: False
#     """
#     display_name = "Mummy's Curse"

#     default = False



@dataclass
class ClankOptions(PerGameCommonOptions):

    # deathlink
    death_link: DeathLink

    # artifacts
    artifacts: Artifacts
    starting_artifacts: StartingArtifacts

    # monkey idol options
    monkey_idols: MonkeyIdols
    monkey_idol_item_behaviour: MonkeyIdolItemBehaviour
    monkey_idol_location_behaviour: MonkeyIdolLocationBehaviour

    # dungeon row options
    dungeon_row: DungeonRow
    row_shuffling_style: RowShufflingStyle
    rowsanity: RowSanity
    pack_size: PackSize

    # bonus row
    bonus_row: BonusRow
    bonus_row_cards: BonusRowCards
    bonus_row_prices: BonusRowPrices


option_groups = [
    OptionGroup("Artifacts", [
        Artifacts,
        StartingArtifacts,
    ]),
    OptionGroup("Idols", [
        MonkeyIdols,
        MonkeyIdolItemBehaviour,
        MonkeyIdolLocationBehaviour,
    ]),
    OptionGroup("Dungeon Row", [
        DungeonRow,
        RowShufflingStyle,
        PackSize,
        RowSanity,
    ]),
    OptionGroup("Bonus Row", [
        BonusRow,
        BonusRowCards,
        BonusRowPrices,
    ]),
]