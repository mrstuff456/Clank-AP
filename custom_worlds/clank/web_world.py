from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

# from .options import option_groups, option_presets


class ClankWebWorld(WebWorld):
    game = "Clank!"
    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Clank for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mrstuff456"],
    )

    tutorials = [setup_en]

    #option_groups = option_groups
    #options_presets = option_presets