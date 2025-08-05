import sys
import os
import pytest
from dataclasses import FrozenInstanceError

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.game_object import GameObject


def test_game_object_creation_and_attributes():
    """
    Tests that a GameObject is created with the correct attributes and that
    the attributes have the correct types.
    """
    game_obj = GameObject(
        name="Test Rock",
        symbol="o",
        description="A rock for testing."
    )

    assert game_obj.name == "Test Rock"
    assert isinstance(game_obj.name, str)
    assert isinstance(game_obj.symbol, str)
    assert isinstance(game_obj.description, str)


def test_game_object_is_frozen():
    """
    Tests that the GameObject is immutable (frozen=True).
    """
    game_obj = GameObject(name="Frozen Object", symbol="F", description="Cannot change.")

    # This test PASSES if a FrozenInstanceError is raised.
    with pytest.raises(FrozenInstanceError):
        game_obj.name = "A new name"
