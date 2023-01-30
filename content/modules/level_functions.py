"""
Module with level building and game functions
"""

# loading level from text file
def load_level(level):
    file_path = "./content/levels/" + level + ".txt"
    with open(file_path, encoding="utf8") as f:
        text = f.read().splitlines()

    new_lines = [line.split('\n', 1)[0].strip() for line in text]
    level = []
    for line in new_lines:
        level.append(line)

    return level


# creating initial setup of maze
from content.modules.classes import TreasureChest, LevelExit, RandomWalkingGuard, SolutionPath
def create_maze(level, wall, guards, treasures, exit, level_size):
    player_coordinates = []
    treasures_coordinates = []
    guards_coordinates = []
    solution_coordinates = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = (-(level_size[1]*12) + 10) + (x*24)
            screen_y = ((level_size[0]*12) - 10) - (y*24) #288 for 25x25

            if character == "X":
                wall.goto(screen_x, screen_y)
                wall.stamp()
                wall.unpassable_position.append((screen_x, screen_y))

            elif character == "S":
                solution_coordinates.append([screen_x, screen_y])
                SolutionPath(screen_x, screen_y)

            elif character == "E":
                exit.append(LevelExit(screen_x, screen_y))

            elif character == "P":
                player_coordinates.append([screen_x, screen_y])
                SolutionPath(screen_x, screen_y)

            elif character == "T":
                treasures_coordinates.append([screen_x, screen_y])

            elif character == "G":
                guards_coordinates.append([screen_x, screen_y])

    for t in treasures_coordinates:
        treasures.append(TreasureChest(t[0], t[1]))
        counter=0
        if [t[0]+24, t[1]] in solution_coordinates:
            counter += 1
        if [t[0]-24, t[1]] in solution_coordinates:
            counter += 1
        if [t[0], t[1]+24] in solution_coordinates:
            counter += 1
        if [t[0], t[1]-24] in solution_coordinates:
            counter += 1
        if counter >= 2:
            SolutionPath(t[0], t[1])


    for g in guards_coordinates:
        guards.append(RandomWalkingGuard(g[0], g[1]))
        counter=0
        if [g[0]+24, g[1]] in solution_coordinates:
            counter += 1
        if [g[0]-24, g[1]] in solution_coordinates:
            counter += 1
        if [g[0], g[1]+24] in solution_coordinates:
            counter += 1
        if [g[0], g[1]-24] in solution_coordinates:
            counter += 1
        if counter >= 2:
            SolutionPath(g[0], g[1])
    
    for guard in guards:
        guard.unpassable_position = wall.unpassable_position

    return player_coordinates[0]


# reading and binding keys as controls
from turtle import listen, onkey
def keyboard_reading(player):
    listen()
    onkey(player.moveUp, "w")
    onkey(player.moveDown, "s")
    onkey(player.moveLeft, "a")
    onkey(player.moveRight, "d")


# moving guards located on current level
from turtle import ontimer
def guards_moving(guards, player):
    for guard in guards:
        guard.player_pos = player
        ontimer(guard.move(), t=250)


# save level score after getting to exit
def save_score(level, score):
    with open(".\content\levels\level_stats.txt", 'w') as f:
        f.write(level + " score:\n" + str(score))


# for chosen difficulty: set size of level (height, width]), number of guards and generate random maze
from content.modules.level_generator import random_maze_generator
from content.modules.level_solver import random_maze_solver
def level_setup(level_name, difficulty):
    
    if difficulty=="easy":
        level_size = [15, 15] 
        guards = 2
        treasures = 3

    elif difficulty == "medium":
        level_size = [20, 30]
        guards = 5
        treasures = 5

    elif difficulty == "hard":
        level_size = [30,45]
        guards = 10
        treasures = 10

    elif difficulty == "extreme":
        level_size = [40, 70]
        guards = 20
        treasures = 15
        
    random_maze_generator(level_size, guards, treasures)
    random_maze_solver(level_name)
