import os
import time

# --- Import Core Classes & Data ---
from game_logic.game_object import GameObject
from game_logic.entities import Entity, ItemEntity
from game_logic.sprite import Sprite
from game_logic.monster import Monster
from game_logic.maps.layered_map import LayeredMap, Layer
from game_logic.game_state import GameState

# --- Import Catalogues ---
from config.monster_catalogue import MONSTERS
from config.items import find_item


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """The main function to initialize and run the game."""
    
    # --- 1. Initialization ---
    
    # Create the game map
    game_map = LayeredMap(width=30, height=20)

    # Create the player's template and instance (Sprite)
    player_template = GameObject(name="Hero", symbol="@", description="Our valiant hero.")
    player = Sprite(base=player_template, x=5, y=5, health=100)
    
    # Create a monster's template and instance
    goblin_template = MONSTERS["Goblin"]
    goblin = Monster(
        base=goblin_template,
        x=15,
        y=10,
        health=goblin_template.base_health
    )
    
    # Place the goblin on the map
    game_map.set_object(goblin.x, goblin.y, Layer.GROUND, goblin)

    # Create the GameState to manage everything
    game_state = GameState(
        current_map=game_map,
        player=player,
        monsters=[goblin]
    )

    # --- 2. The Main Game Loop ---
    
    print("Dungeon Crawl! Your adventure begins.")
    time.sleep(2)

    while True:
        clear_screen()
        
        # Update player's position on the map for drawing
        game_state.current_map.player_x = game_state.player.x
        game_state.current_map.player_y = game_state.player.y

        # Display the current state of the map
        print("--- Your View ---")
        game_state.current_map.display_map(
            view_x=game_state.player.x,
            view_y=game_state.player.y,
            view_width=20,
            view_height=10
        )
        print("-----------------")
        
        # Display Player Status
        print(f"Health: {game_state.player.health}/100 | Position: ({game_state.player.x}, {game_state.player.y})")
        
        # Prompt for player input
        action = input("> ").lower().strip()

        # --- 3. Process Input (This is where the PlayerParser will go) ---
        
        if action in ["n", "north"]:
            game_state.player.y -= 1
        elif action in ["s", "south"]:
            game_state.player.y += 1
        elif action in ["w", "west"]:
            game_state.player.x -= 1
        elif action in ["e", "east"]:
            game_state.player.x += 1
        elif action == "quit":
            print("You flee the dungeon. Farewell, adventurer!")
            break
        else:
            print("Unknown command.")
            time.sleep(1) # Pause to let the player read the message


if __name__ == "__main__":
    main()
