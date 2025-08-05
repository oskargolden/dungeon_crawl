import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.game_object import GameObject # ignore: type


game_obj1 = GameObject('test_object', 'T', 'This is a test object')


def test_game_object():
    assert type(game_obj1.name) == str
    assert type(game_obj1.symbol) == str
    assert type(game_obj1.description) == str
    
def test_game_object_repr():
    assert repr(game_obj1) == "GameObject(name='test_object', symbol='T', description='This is a test object')"