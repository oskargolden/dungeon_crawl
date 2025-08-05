# game_logic/game_object.py
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class GameObject():
    """A template for the intrinsic, immutable properties of an object type.

    This class serves as a frozen blueprint for all items, characters, and
    other objects in the game. It defines the core, unchangeable data that
    is shared by all instances of a particular type. For example, all
    "Sword" items will share the same base GameObject template.

    Attributes:
        name (str): The common name of the object (e.g., "Sword").
        symbol (str): The single character used to represent this object on
            the game map.
        description (str): A detailed description of the object, which could
            be shown to the player upon inspection.
    """
    name: str
    symbol: str  # The character used to draw it on the map
    description: str