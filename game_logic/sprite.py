from dataclasses import dataclass, asdict, field
from config.items import ITEMS


@dataclass
class Sprite:
    xp: int = 0
    lvl: int = 0
    # The inventory is now a dictionary with a comprehensive list of items,
    # all set to a default count of 0.
    inventory: dict = field(default_factory=lambda: {item.name: 0 for item in ITEMS})
    wearing: dict = field(default_factory=lambda: {
        'head': None, 'chest': None, 'arms': None, 'wrists': None,
        'hands': None, 'legs': None, 'feet': None, 'neck': None,
        'finger_left': None, 'finger_right': None, 'waist': None,
        'shoulders': None, 'back': None,
    })
    stats: dict = field(default_factory=lambda: {
        'strength': 0, 'dexterity': 0, 'constitution': 0,
        'intelligence': 0, 'wisdom': 0, 'charisma': 0
    })
    skills: dict = field(default_factory=lambda: {
        'acrobatics': 0, 'athletics': 0, 'deception': 0,
        'insight': 0, 'intimidation': 0, 'investigation': 0,
        'perception': 0, 'persuasion': 0, 'stealth': 0,
        'survival': 0,
    })
    x: int = field(default=None)
    y: int = field(default=None)
    z: int = field(default=None)
    health: int = field(default=None)
    speed: int = field(default=None)

    def to_dict(self):
        """Converts the Sprite object to a dictionary."""
        return asdict(self)
