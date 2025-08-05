# In a new file, e.g., game_logic/actor.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from game_logic.game_object import GameObject  # Import the new base class


@dataclass
class Actor(GameObject):
    """
    Represents any creature or character that can act, have stats,
    and carry an inventory. Inherits from GameObject.
    """
    xp: int = 0
    lvl: int = 0
    health: int = 10
    speed: int = 10

    # The inventory is a LIST of GameObject instances
    inventory: List[GameObject] = field(default_factory=list)

    wearing: Dict[str, Optional[GameObject]] = field(default_factory=lambda: {
        'head': None, 'chest': None, 'arms': None, 'wrists': None,
        'hands': None, 'legs': None, 'feet': None, 'neck': None,
        'finger_left': None, 'finger_right': None, 'waist': None,
        'shoulders': None, 'back': None,
    })

    stats: Dict[str, int] = field(default_factory=lambda: {
        'strength': 10, 'dexterity': 10, 'constitution': 10,
        'intelligence': 10, 'wisdom': 10, 'charisma': 10
    })

    skills: Dict[str, int] = field(default_factory=dict)

    def to_dict(self):
        # You'll need a custom method for this now that you have nested objects
        # asdict() might not behave as you expect with complex types.
        pass
