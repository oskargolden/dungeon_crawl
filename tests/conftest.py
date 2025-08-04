# tests/conftest.py (write once)
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# test_sprite.py (clean!)
from game_logic.sprite import Sprite

# test_layered_maps.py (clean!)
from game_logic.maps.layered_map import LayeredMap
