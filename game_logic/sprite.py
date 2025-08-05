from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional
from config.items import ITEMS
from game_logic.game_object import GameObject


@dataclass
class Sprite(GameObject):
    xp: int = 0
    lvl: int = 0
    health: int = 10
    speed: int = 10
    # The inventory is now a dictionary with a comprehensive list of items,
    # all set to a default count of 0.
    # The inventory is a LIST of GameObject instances
    inventory: List[GameObject] = field(default_factory=list)
    wearing: Dict[str, Optional[GameObject]] = field(default_factory=lambda: {
        'head': None, 'chest': None, 'arms': None, 'wrists': None,
        'hands': None, 'legs': None, 'feet': None, 'neck': None,
        'finger_left': None, 'finger_right': None, 'waist': None,
        'shoulders': None, 'back': None,
    })
    stats: Dict[str, int] = field(default_factory=lambda: {
        'strength': 0, 'dexterity': 0, 'constitution': 0,
        'intelligence': 0, 'wisdom': 0, 'charisma': 0
    })
    skills: Dict[str, int] = field(default_factory=lambda: {
        'acrobatics': 0, 'athletics': 0, 'deception': 0,
        'insight': 0, 'intimidation': 0, 'investigation': 0,
        'perception': 0, 'persuasion': 0, 'stealth': 0,
        'survival': 0,
    })

    def to_dict(self):
        # You'll need a custom method for this now that you have nested objects
        # asdict() might not behave as you expect with complex types.
        pass
