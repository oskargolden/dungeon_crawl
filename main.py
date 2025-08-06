import os
import time

# --- Import Core Classes & Data ---
from game_logic.game_object import GameObject
from game_logic.entities import Entity, ItemEntity
from game_logic.sprite import Sprite
from game_logic.monster import Monster
from game_logic.maps.layered_map import LayeredMap, Layer
from game_logic.game_state import GameState
from game_logic.command_parser import CommandParser
from game_logic.actions import handle_movement, handle_inventory, handle_take_item

# --- Import Catalogues ---
from config.monster_catalogue import MONSTERS
from config.items import find_item

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """The main function to initialize and run the game."""

    # --- 1. Initialization ---

    game_map = LayeredMap(width=30, height=20)
    player_template = GameObject(name="Hero", symbol="@", description="Our valiant hero.")
    player = Sprite(base=player_template, x=5, y=5, health=100)

    goblin_template = MONSTERS["Goblin"]
    goblin = Monster(base=goblin_template, x=15, y=10, health=goblin_template.base_health)
    game_map.set_object(goblin.x, goblin.y, Layer.GROUND, goblin)

    # --- NEW: Add an item to the map for the player to pick up ---
    sword_template = find_item("Sword")
    sword_on_ground = ItemEntity(base=sword_template, x=7, y=5)
    game_map.set_object(sword_on_ground.x, sword_on_ground.y, Layer.GROUND, sword_on_ground)

    game_state = GameState(
        current_map=game_map,
        player=player,
        monsters=[goblin]
    )
    
    parser = CommandParser()

    # --- 2. The Main Game Loop ---
    
    print("Dungeon Crawl! Your adventure begins.")
    time.sleep(2)

    while True:
        clear_screen()
        
        game_state.current_map.player_x = game_state.player.x
        game_state.current_map.player_y = game_state.player.y

        print("--- Your View ---")
        game_state.current_map.display_map(
            view_x=game_state.player.x,
            view_y=game_state.player.y,
            view_width=20,
            view_height=10
        )
        print("-----------------")

        print(f"Health: {game_state.player.health}/100 | Position: ({game_state.player.x}, {game_state.player.y})")

        action = input("> ").lower().strip()
        command = parser.parse(action)

        # --- 3. Process Parsed Command ---

        if command:
            if command.verb == "move":
                handle_movement(game_state, command.noun)
                time.sleep(0.5)
            elif command.verb == "inventory":
                handle_inventory(game_state)
                input("\nPress Enter to continue...")
            # --- NEW: Handle the 'take' command ---
            elif command.verb == "take":
                if command.noun:
                    handle_take_item(game_state, command.noun)
                else:
                    print("What do you want to take?")
                time.sleep(1)
            elif command.verb == "exit":
                print("You flee the dungeon. Farewell, adventurer!")
                break
            else:
                print("Unknown command.")
                time.sleep(1)


if __name__ == "__main__":
    main()
