# cofrom nfig/templates.py
"""Defines the hierarchy of immutable template classes for NPCs and monsters."""

from dataclasses import dataclass, field
from typing import List, Dict, Any
from enum import Enum, auto
from game_logic.game_object import GameObject


# --- BEHAVIOR, TYPE, AND ABILITY ENUMS ---

class MonsterBehavior(Enum):
    """Defines the default AI behavior of an NPC."""
    HOSTILE = auto()  # Attacks on sight.
    NEUTRAL = auto()  # Ignores unless attacked.
    FLEE = auto()     # Tries to run away from threats.
    GUARD = auto()    # Stays in one area and attacks if approached.


class MonsterType(Enum):
    """Defines the categorical type of a monster for spell/ability interactions."""
    ABERRATION = auto()
    BEAST = auto()
    CONSTRUCT = auto()
    DRAGON = auto()
    ELEMENTAL = auto()
    GIANT = auto()
    HUMANOID = auto()
    MONSTROSITY = auto()
    OOZE = auto()
    UNDEAD = auto()


class SpecialAbility(Enum):
    """Defines special abilities a monster might have."""
    PARALYZE = auto()
    PETRIFY = auto()
    LIFE_DRAIN = auto()

# --- TEMPLATE HIERARCHY ---


@dataclass(frozen=True, slots=True)
class NPCTemplate(GameObject):
    """
    Base template for all non-player characters.

    Attributes:
        behavior (MonsterBehavior): The default AI behavior of the NPC.
        base_health (int): The base health points for this NPC type.
        base_stats (Dict[str, int]): A dictionary of base ability scores.
        loot_table (List[str]): A list of item names this NPC might drop.
    """
    behavior: MonsterBehavior
    base_health: int
    base_stats: Dict[str, int]
    loot_table: List[str]


@dataclass(frozen=True, slots=True)
class MonsterTemplate(NPCTemplate):
    """
    A template specifically for hostile or potentially hostile monsters.

    Inherits from NPCTemplate and adds attributes relevant for combat.

    Attributes:
        monster_type (MonsterType): The monster's categorical type.
        base_attack (int): The base damage value for the monster's attack.
        base_defense (int): The base defense or armor value for the monster.
        special_abilities (List[SpecialAbility]): A list of special abilities.
    """
    monster_type: MonsterType
    base_attack: int
    base_defense: int
    special_abilities: List[SpecialAbility] = field(default_factory=list)




