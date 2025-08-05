from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from game_logic.game_object import GameObject

# Assumes GameObject class exists, for example in:
# from game_logic.game_object import GameObject



class Layer(Enum):
    """An Enum to represent the distinct layers on a map tile."""
    GROUND = "ground"
    AIR = "air"
    CEILING = "ceiling"


@dataclass
class LayeredTile:
    """Represents all layers for a single cell, now holding GameObjects."""
    ground: Optional[GameObject] = None
    air: Optional[GameObject] = None
    ceiling: Optional[GameObject] = None


class LayeredMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # Corrected 2D data structure: [y][x]
        self.tiles: List[List[LayeredTile]] = [
            [LayeredTile() for _ in range(width)] for _ in range(height)
        ]
        # Player location can be stored on the Player/Actor object itself
        # Or here if the map needs to be aware of it.
        self.player_x = 1
        self.player_y = 1

    def get_object(self, x: int, y: int, layer: Layer) -> Optional[GameObject]:
        """Gets the GameObject from a specific layer of the tile at (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            tile = self.tiles[y][x]
            return getattr(tile, layer.value)
        return None  # Out of bounds

    def set_object(self, x: int, y: int, layer: Layer, obj: Optional[GameObject]):
        """Places a GameObject onto a specific layer of the tile at (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            tile = self.tiles[y][x]
            setattr(tile, layer.value, obj)

    def display_map(self, view_x: int, view_y: int, view_width: int, view_height: int):
        """
        Displays a portion of the map centered around (view_x, view_y).
        It prioritizes drawing objects in the AIR layer, then GROUND.
        """
        start_x = max(0, view_x - view_width // 2)
        start_y = max(0, view_y - view_height // 2)
        end_x = min(self.width, start_x + view_width)
        end_y = min(self.height, start_y + view_height)

        for y in range(start_y, end_y):
            row_str = ""
            for x in range(start_x, end_x):
                char_to_draw = ' '
                # Check air layer first
                air_obj = self.get_object(x, y, Layer.AIR)
                if air_obj:
                    char_to_draw = air_obj.symbol
                else:
                    # Otherwise, check ground layer
                    ground_obj = self.get_object(x, y, Layer.GROUND)
                    if ground_obj:
                        char_to_draw = ground_obj.symbol
                    else:
                        # If nothing is there, draw a default floor tile
                        char_to_draw = '.'

                # Draw the player character
                if x == self.player_x and y == self.player_y:
                    char_to_draw = '@'

                row_str += char_to_draw
            print(row_str)

    def draw_entire_map(self):
        pass
