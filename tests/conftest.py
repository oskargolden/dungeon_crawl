import sys
import os
import pytest

# Add the project root directory to the Python path so we can find our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.game_object import GameObject
from game_logic.entities import Entity, ItemEntity
from game_logic.sprite import Sprite
from config.items import Weapon


@pytest.fixture
def player_template() -> GameObject:
    """A fixture that returns a frozen GameObject template for a player."""
    return GameObject(name="Hero", symbol="@", description="Our valiant hero.")


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


@pytest.fixture
def basic_sprite(player_template: GameObject) -> Sprite:
    """
    A fixture that returns a mutable Sprite instance created from the
    player_template. This is a ready-to-use character for tests.
    """
    return Sprite(
        base=player_template,
        x=5,
        y=5,
        z=0,
        health=100
    )
