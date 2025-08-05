from dataclasses import dataclass, field
from typing import List
from game_logic.NPC_actor import NPCActor


@dataclass
class Monster(NPCActor):
    """
    Represents a hostile NPC in the game world.

    Inherits from NPCActor, gaining all the base properties of a character,
    and adds monster-specific attributes like attack power and loot.

    Attributes:
        attack_power (int): The base damage value for the monster's attack.
        defense (int): The base defense or armor value for the monster.
        loot (List[str]): A list of item names that this monster might drop.
    """
    attack_power: int = 1
    defense: int = 1
    loot: List[str] = field(default_factory=list)
