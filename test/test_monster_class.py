import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import all the classes in the inheritance chain to test against them
from game_logic.game_object import GameObject
from game_logic.entities import Entity
from game_logic.sprite import Sprite
from game_logic.NPC_actor import NPCActor
from game_logic.monster import Monster


def test_monster_inheritance():
    """
    Tests that the Monster class correctly inherits from all its parent classes.
    """
    # Create a simple template and a monster instance for the test
    monster_template = GameObject(name="Goblin", symbol="g", description="A lowly goblin")
    goblin_instance = Monster(base=monster_template)

    # Assert that the monster IS an instance of all its parent classes
    assert isinstance(goblin_instance, Monster)
    assert isinstance(goblin_instance, NPCActor)
    assert isinstance(goblin_instance, Sprite)
    assert isinstance(goblin_instance, Entity)


def test_monster_default_attributes():
    """
    Tests that a Monster instance has the correct default attributes from
    its own class and its parent classes.
    """
    monster_template = GameObject(name="Orc", symbol="o", description="A brutish orc.")
    orc_instance = Monster(base=monster_template)

    # Test attributes from the Monster class itself
    assert orc_instance.attack_power == 1
    assert orc_instance.defense == 1
    assert isinstance(orc_instance.loot, list)
    assert len(orc_instance.loot) == 0

    # Test attributes inherited from the Sprite class
    assert orc_instance.health == 10
    assert isinstance(orc_instance.stats, dict)
    assert orc_instance.stats['strength'] == 0

    # Test attributes inherited from the Entity class
    assert orc_instance.base.name == "Orc"
    assert orc_instance.x is None
