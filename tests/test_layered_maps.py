# In your test_layered_maps.py
from game_logic.game_object import GameObject  # Import the real class
from game_logic.maps.layered_map import Layer, LayeredTile, LayeredMap

# Dummy objects to use in your tests
dummy_rock = GameObject(name="Rock", symbol="o", description="A simple rock.")
dummy_bird = GameObject(name="Bird", symbol="b", description="A bird in the sky.")

# How to test the new LayeredTile
tile = LayeredTile()
assert tile.ground is None
assert tile.air is None
assert tile.ceiling is None

# The updated test for Layer enum
assert Layer.GROUND.value == "ground"
assert Layer.AIR.value == "air"

# How to test the new 2D structure
map_obj = LayeredMap(width=10, height=5)
assert len(map_obj.tiles) == 5  # Number of rows (height)
assert len(map_obj.tiles[0]) == 10  # Number of columns (width)
assert isinstance(map_obj.tiles[0][0], LayeredTile)

# A new "round trip" test will look like this
map_obj.set_object(2, 2, Layer.GROUND, dummy_rock)
retrieved_obj = map_obj.get_object(2, 2, Layer.GROUND)
assert retrieved_obj is dummy_rock  # Use 'is' to check it's the exact same object


"""
Key Test Cases to Write:
1. LayeredTile Tests:

Default values test: Verify new tile has correct defaults
Custom values test: Create tile with specific symbols
Immutability test: Ensure you can modify the fields

2. Layer Enum Tests:
Enum values test: Verify GROUND=0, AIR=1, CEILING=2
Enum access test: Test Layer.GROUND.value returns 0

3. LayeredMap Initialization Tests:

Basic creation: Create 5x5 map, verify dimensions
Tiles structure: Verify tiles array has correct 3D structure
Player defaults: Check player starts at (1,1) on GROUND layer
Tile defaults: Verify all tiles start with default LayeredTile values

4. get_tile() Method Tests:

Get ground tile: Retrieve ground symbol from a position
Get air tile: Retrieve air symbol from same position
Get ceiling tile: Retrieve ceiling symbol from same position
Default symbols: Verify getting from unmodified position returns defaults
Boundary test: Test getting from (0,0) and (width-1, height-1)

5. set_tile() Method Tests:

Set ground tile: Change ground symbol, verify it changed
Set air tile: Change air symbol, verify only air changed
Set ceiling tile: Change ceiling symbol, verify only ceiling changed
Multiple layers: Set different symbols on all 3 layers at same position
Isolation test: Verify changing one layer doesn't affect others

6. Integration Tests:

Round trip: Set a tile, then get it back, verify they match
Different positions: Set tiles at different coordinates, verify independence
Layer independence: Modify ground at (1,1), verify air/ceiling at (1,1) unchanged

7. Edge Case Tests:

Boundary positions: Test (0,0) and (width-1, height-1)
All layer types: Ensure each Layer enum value works with both methods

"""
