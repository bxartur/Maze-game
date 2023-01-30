from content.modules.window import game_window
from content.modules.classes import Wall, Player
from content.modules.level_functions import *

def maze_game(level_name):

    level = load_level(level_name)
    level_size = [len(level), len(level[0])]
    window = game_window(level_size)

    wall = Wall()
    treasures, guards, exits = [], [], []
    starting_position = create_maze(level, wall, guards, treasures, exits, level_size)
    player = Player()
    player.unpassable_position = wall.unpassable_position
    player.goto(starting_position)

    keyboard_reading(player)
    guards_moving(guards, player)

    while True:
        for treasure in treasures:
            if player.collides(treasure):
                player.score += treasure.award
                print("Level score:", player.score)
                treasure.hideturtle()
                treasures.remove(treasure)

        for guard in guards:
            if player.collides(guard):
                print("You got caught by guard")
                window.bye()
                return 'captured'
            
        for exit in exits:
            if player.collides(exit):
                save_score(level_name, player.score)
                window.bye()
                print("Final level score:", player.score)
                return 'escaped'

        window.update()

