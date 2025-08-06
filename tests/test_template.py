import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Import all the necessary classes and data ---
from game_logic.game_object import GameObject
from config.templates import (
    NPCTemplate, MonsterTemplate, MonsterBehavior, MonsterType, SpecialAbility
)
from config.npc_catalogue import NPCS, TOWNSFOLK
from config.monster_catalogue import MONSTERS, SKELETON, GOBLIN

# --- Tests for the Template Hierarchy ---


def test_template_inheritance():
    """
    Tests that the MonsterTemplate class correctly inherits from its parents.
    This also implicitly tests that the non-default argument error is fixed.
    """
    # If this object can be created, the TypeError is resolved.
    test_monster = MonsterTemplate(
        name="Test", symbol="t", description="A test monster.",
        monster_type=MonsterType.BEAST,
        behavior=MonsterBehavior.NEUTRAL,
        base_health=10,
        base_attack=5,
        base_defense=5,
        base_stats={},
        loot_table=[]

    )

    # Assert that the monster IS an instance of all its parent template classes
    assert isinstance(test_monster, MonsterTemplate)
    assert isinstance(test_monster, NPCTemplate)
    assert isinstance(test_monster, GameObject)

# --- Tests for the NPC Catalogue ---


def test_npc_catalogue_data():
    """
    Tests the data integrity of a sample NPC from the catalogue.
    """
    assert TOWNSFOLK.name == "Townsfolk"
    assert TOWNSFOLK.behavior == MonsterBehavior.NEUTRAL
    assert TOWNSFOLK.base_health == 8
    
    # Test the master dictionary
    assert NPCS["Townsfolk"] is TOWNSFOLK

# --- Tests for the Monster Catalogue ---


def test_monster_catalogue_data():
    """
    Tests the data integrity of a sample monster from the catalogue.
    """
    assert SKELETON.name == "Skeleton"
    assert SKELETON.monster_type == MonsterType.UNDEAD
    assert SKELETON.behavior == MonsterBehavior.HOSTILE
    assert SKELETON.base_attack == 5

    # Test the master dictionary
    assert MONSTERS["Skeleton"] is SKELETON
    assert MONSTERS["Goblin"].name == "Goblin"  # Another way to check
