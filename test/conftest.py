import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.game_object import GameObject
from config.items import Weapon
from game_logic.entities import Entity, ItemEntity
from game_logic.sprite import Sprite
from game_logic.monster import Monster # <-- New import


# --- Character Fixtures ---

@pytest.fixture
def player_template() -> GameObject:
    """A fixture that returns a frozen GameObject template for a player."""
    return GameObject(name="Hero", symbol="@", description="Our valiant hero.")


@pytest.fixture
def basic_sprite(player_template: GameObject) -> Sprite:
    """A fixture that returns a mutable Sprite instance for a player."""
    return Sprite(
        base=player_template,
        x=5, y=5, z=0,
        health=100
    )


# --- Monster Fixtures ---

@pytest.fixture
def goblin_template() -> GameObject:
    """A fixture that returns a frozen GameObject template for a monster."""
    return GameObject(name="Goblin", symbol="g", description="A lowly goblin.")


@pytest.fixture
def goblin_instance(goblin_template: GameObject) -> Monster:
    """A fixture that returns a mutable Monster instance for a goblin."""
    return Monster(
        base=goblin_template,
        x=10, y=10, z=0,
        health=25,
        attack_power=5,
        defense=2
    )


# --- Item Fixtures ---

@pytest.fixture
def sword_template() -> Weapon:
    """A fixture that returns a frozen Weapon template for a sword."""
    return Weapon(
        name='Sword',
        symbol='/',
        description='A standard longsword.',
        cost=10,
        weight=60,
        damage='1d8',
        qualities=['Melee'],
    )
