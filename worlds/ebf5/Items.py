
from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Item, ItemClassification

class EBF5Item(Item):
    game: str = "Epic Battle Fantasy 5"
    
class EBF5ItemCategory(IntEnum):
    # Main Categories
    KEY_ITEM    = 0
    KEY         = 1 # as in keys for blocks
    EQUIPMENT   = 2
    CARD        = 3
    SKILL       = 4
    ITEM        = 5 # food, stat boosters ect.

    # Sub Categories
    SWORD       = 6
    STAFF       = 7
    GUN         = 8
    BOW         = 9
    TOY         = 10
    # ... TODO: Add everything else

class ItemData(NamedTuple):
    name: str
    sid: Optional[str] # In-Game SID, required to match the item in game
    category: list[EBF5ItemCategory]
    classification: ItemClassification
    is_unique: bool = True
    max_amount: int = 1

all_items = [] # TODO...

key_items = [
    ItemData("Magnet Boots", "magneticboots", [EBF5ItemCategory.KEY_ITEM], ItemClassification.progression)
    # On and On...
]

equipment_items = [
    # ...
]
