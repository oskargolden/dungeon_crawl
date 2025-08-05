from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional
from config.items import ITEMS
from game_logic.entities import Entity, ItemEntity
from game_logic.game_object import GameObject



@dataclass
class Sprite(Entity):
    """
    Represents an actor in the game world, such as a player or monster.

    A Sprite is a mutable, in-game entity that can act and has a state that
    can change (e.g., health, inventory). It inherits its core instance
    properties (a base template and location) from the Entity class.

    Attributes:
        xp (int): The character's current experience points.
        lvl (int): The character's current level.
        health (int): The character's current health points.
        speed (int): A value determining the character's initiative or
            movement speed.
        inventory (List[ItemEntity]): A list of the unique ItemEntity objects
            that the character is carrying.
        wearing (Dict[str, Optional[ItemEntity]]): A dictionary mapping
            equipment slots (e.g., 'head', 'chest') to the ItemEntity
            equipped in that slot, or None if the slot is empty.
        stats (Dict[str, int]): A dictionary for the character's core
            ability scores (e.g., 'strength', 'dexterity').
        skills (Dict[str, int]): A dictionary for the character's skills
            (e.g., 'acrobatics', 'stealth').
    """
    
    xp: int = 0
    lvl: int = 0
    health: int = 10
    speed: int = 10
    inventory: List[ItemEntity] = field(default_factory=list)
    wearing: Dict[str, Optional[ItemEntity]] = field(default_factory=lambda: {
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
        'survival': 0, 'combat': 0, 'magic': 0, 'crafting': 0,
        'healing': 0, 'nature': 0, 'religion': 0, 'history': 0,
        'technology': 0, 'social': 0, 
    })

    def to_dict(self):
        """
        Serializes the Sprite object and its contents into a dictionary.

        This method creates a dictionary representation of the sprite, suitable
        for saving game state. It recursively calls .to_dict() on nested
        objects like items in the inventory.

        Returns:
            Dict: A dictionary containing the sprite's data.
        """
        return {
            'name': self.base.name,
            'symbol': self.base.symbol,
            'description': self.base.description,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'xp': self.xp,
            'lvl': self.lvl,
            'health': self.health,
            'speed': self.speed,
            'inventory': [item.to_dict() for item in self.inventory],
            'wearing': {
                slot: item.to_dict() if item else None
                for slot, item in self.wearing.items()
            },
            'stats': self.stats.copy(),
            'skills': self.skills.copy(),
        }
        
