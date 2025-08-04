from game_logic.maps.layered_map import Layer, LayeredTile, LayeredMap


class TestLayeredTile:
    def test_layered_tile(self):
        assert LayeredTile.ground == '.'
        assert LayeredTile.air == ' '
        assert LayeredTile.ceiling == '.'


class TestLayer:
    def test_layer_enum(self):
        assert Layer.GROUND.value == 0
        assert Layer.AIR.value == 1
        assert Layer.CEILING.value == 2


class TestlayeredMap:

    def test_layered_map_size(self):
        map_obj = LayeredMap(5, 5)
        assert map_obj.width == 5
        assert map_obj.height == 5


"""
Key Test Cases to Write:
1. LayeredTile Tests:

Default values test: Verify new tile has correct defaults
Custom values test: Create tile with specific symbols
Immutability test: Ensure you can modify the fields

2. Layer Enum Tests:
Enum values test: Verify GROUND=0, AIR=1, CEILING=2 +===========+ DONE
Enum access test: Test Layer.GROUND.value returns 0 +===========+ DONE

3. LayeredMap Initialization Tests:

Basic creation: Create 5x5 map, verify dimensions +=============+ DONE
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
