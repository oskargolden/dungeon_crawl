from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from game_logic.game_object import GameObject
from game_logic.entities import Entity


@dataclass
class Layer(Enum):
    """An Enum representing the distinct layers on a map tile."""
    # --- Physical Object Layers ---
    GROUND = "ground"      # For solid objects, items, and characters on the floor.
    LIQUID = "liquid"      # For pools of water, lava, etc.
    DETAIL = "detail"      # For non-interactive scenery and clutter.

    # --- Gameplay and Logic Layers ---
    BLOCKING = "blocking"  # For invisible walls and impassable terrain.
    TRIGGER = "trigger"    # For invisible pressure plates, traps, and event triggers.
    EFFECTS = "effects"    # For temporary spells, gas clouds, etc.

    # --- Vertical Layers ---
    AIR = "air"            # For flying creatures, ropes, etc.
    CEILING = "ceiling"    # For chandeliers, stalactites, etc.


@dataclass
class LayeredTile:
    """Represents all layers for a single cell, holding Entity instances."""
    # --- Physical Object Layers ---
    ground: Optional[Entity] = None
    liquid: Optional[Entity] = None
    detail: Optional[Entity] = None  # THis is where the Scenery class goes.

    # --- Gameplay and Logic Layers ---
    blocking: Optional[Entity] = None
    trigger: Optional[Entity] = None
    effects: Optional[Entity] = None

    # --- Vertical Layers ---
    air: Optional[Entity] = None
    ceiling: Optional[Entity] = None


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
                    char_to_draw = air_obj.base.symbol
                else:
                    # Otherwise, check ground layer
                    ground_obj = self.get_object(x, y, Layer.GROUND)
                    if ground_obj:
                        char_to_draw = ground_obj.base.symbol
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
