"""
This module contains functions that execute player commands and modify the game state.
"""
from game_logic.game_state import GameState
from game_logic.maps.layered_map import Layer
from game_logic.entities import ItemEntity


def handle_movement(game_state: GameState, direction: str):
    """Handles the player's movement command.

    Args:
        game_state (GameState): The current state of the game.
        direction (str): The direction to move ('north', 'south', 'east', 'west').
    """
    player = game_state.player
    game_map = game_state.current_map

    # Determine the new coordinates based on direction
    new_x, new_y = player.x, player.y
    if direction == "north":
        new_y -= 1
    elif direction == "south":
        new_y += 1
    elif direction == "west":
        new_x -= 1
    elif direction == "east":
        new_x += 1

    # Check for map boundaries
    if not (0 <= new_x < game_map.width and 0 <= new_y < game_map.height):
        print("You can't go that way.")
        return

    # Check for blocking objects
    blocking_obj = game_map.get_object(new_x, new_y, Layer.BLOCKING)
    ground_obj = game_map.get_object(new_x, new_y, Layer.GROUND)

    # For now, let's say any monster blocks movement.
    # We can make this more complex later.
    if blocking_obj or (ground_obj and ground_obj in game_state.monsters):
        print("Something is blocking your way.")
        return

    # If the move is valid, update the player's position
    player.x = new_x
    player.y = new_y
    print(f"You move {direction}.")


def handle_inventory(game_state: GameState):
    """Handles the player's inventory command."""
    player = game_state.player

    if not player.inventory:
        print("Your inventory is empty.")
        return

    print("You are carrying:")
    for item_entity in player.inventory:
        # We use the .name property, which correctly gets the name
        # from the base template.
        print(f"- {item_entity.name}")


def handle_take_item(game_state: GameState, item_name: str):
    """Handles the player's command to take an item from the ground.

    Args:
        game_state (GameState): The current state of the game.
        item_name (str): The name of the item the player is trying to take.
    """
    player = game_state.player
    game_map = game_state.current_map

    # Check for an object on the ground layer at the player's position
    ground_obj = game_map.get_object(player.x, player.y, Layer.GROUND)

    if not ground_obj:
        print("There is nothing here to take.")
        return

    # Check if the object is an item (and not a monster, for example)
    if not isinstance(ground_obj, ItemEntity):
        print(f"You can't take the {ground_obj.name}.")
        return

    # Check if the item's name matches the command
    if item_name.lower() in ground_obj.name.lower():
        # Remove the item from the map
        game_map.set_object(player.x, player.y, Layer.GROUND, None)
        # Add the item to the player's inventory
        player.inventory.append(ground_obj)
        print(f"You take the {ground_obj.name}.")
    else:
        print(f"You don't see a {item_name} here.")

