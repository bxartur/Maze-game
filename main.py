"""
Main file that provides:
    - launching game on selected level
    - information whether player hit finish or got captured
"""

from content.maze_game import maze_game
from content.modules.level_functions import level_setup

def main_game(level_name, difficulty):
    if level_name == "generated":
        level_setup("level_" + level_name, difficulty)

    if difficulty in ["easy"]:
        return maze_game("level_" + level_name + "_solved")
    else:
        return maze_game("level_" + level_name)
    

# levels: 1(test level), generated
level_name = "generated"

# difficulties: easy, medium, hard, extreme
difficulty = "medium"

# result options: 'captured' or 'escaped'
game_result = main_game(level_name, difficulty)