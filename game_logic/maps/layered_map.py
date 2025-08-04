# game_logic/maps/layered_map.py
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

GROUND_LEVEL = 0
AIR_LEVEL = 1
CEILING_LEVEL = 2


# Enums here create named constants making it easier to use.
# Instead of writing 0 you can write Layer.GROUND (Layer.GROUND.value returns 0)
class Layer(Enum):
    GROUND = 0
    AIR = 1
    CEILING = 2


@dataclass
class LayeredTile:
    ground: str = '.'     # Floor, pit, water, etc.
    air: str = ' '        # Empty air, flying creature, rope, etc.
    ceiling: str = '.'    # Normal ceiling, stalactite, chandelier, etc.


class LayeredMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # 3D: [layer][y][x]
        self.tiles = [
            [[LayeredTile() for x in range(width)] for y in range(height)]
            for layer in range(3)
        ]
        self.player_x = 1
        self.player_y = 1
        self.player_layer = Layer.GROUND

    def get_tile(self, x: int, y: int, layer: Layer) -> str:
        tile = self.tiles[layer.value][y][x]
        if layer == Layer.GROUND:
            return tile.ground
        elif layer == Layer.AIR:
            return tile.air
        else:
            return tile.ceiling

    def set_tile(self, x: int, y: int, layer: Layer, symbol: str):
        tile = self.tiles[layer.value][y][x]
        if layer == Layer.GROUND:
            tile.ground = symbol
        elif layer == Layer.AIR:
            tile.air = symbol
        else:
            tile.ceiling = symbol
