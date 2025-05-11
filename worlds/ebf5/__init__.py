from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.ebf5.Options import EpicBattleFantasy5Options

class EpicBattleFantasy5Web(WebWorld):
    theme = "jungle"
    # TODO: Make this more accurate
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the the EBF5 Randomiser on your computer.",
        "English",
        "setup_en",
        "setup/en",
        ["NitroTears"]
    )]


class EpicBattleFantasy5World(World):
    """
    A turn-based RPG adventure, full of video game references, juvenile dialogue, and anime fanservice... 
    and also strategic combat, monster catching, and tons of treasure hunting!
    """
    game = "Epic Battle Fantasy 5"
    web = EpicBattleFantasy5Web()
    options_dataclass = EpicBattleFantasy5Options
    options: EpicBattleFantasy5Options


    