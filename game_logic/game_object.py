#  game_logic.game_object
from dataclasses import dataclass, field


@dataclass
class GameObject(frozen=True, slots=True):
    """The absolute base class for any object in the game world."""
    name: str
    symbol: str  # The character used to draw it on the map
    description: str
    x: int = field(default=None, repr=False)  # Position is not always needed
    y: int = field(default=None, repr=False)
    z: int = field(default=None, repr=False)
