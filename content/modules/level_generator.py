from random import choice
from math import sqrt

# return number of cells around wall
def surroundingCells(maze, wall, cell_symbol):
	counter = 0
	if (maze[wall[0]-1][wall[1]] == cell_symbol):
		counter += 1
	if (maze[wall[0]+1][wall[1]] == cell_symbol):
		counter += 1
	if (maze[wall[0]][wall[1]-1] == cell_symbol):
		counter +=1
	if (maze[wall[0]][wall[1]+1] == cell_symbol):
		counter += 1
	return counter

# make safe zone for player, guards must resp outside of the zone at start of level
def initial_guard_distance(player, guard):
    x = player[1] - guard[1]
    y = player[0] - guard[0]
    if (sqrt((x**2) + (y**2)) > 10):
        return True
    else: 
        return False



# convert maze to string and save to file
def save_generated_level(maze_list):
	str_maze = ""
	for line in maze_list:
		str_maze += (''.join(line)) + '\n'

	with open(".\content\levels\level_generated.txt", 'w') as file:
		file.write(str_maze[:-1])


def random_maze_generator(maze_size, guards, treasures):
	
	height=maze_size[0]
	width=maze_size[1]

	wall_symbol = 'X'
	cell_symbol = ' '
	unvisited_symbol = 'u'

	maze, walls = [], []

	# mark all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited_symbol)
		maze.append(line)

	# randomize initial point and set it a cell
	initial_height = choice(range(1, height-2))
	initial_width = choice(range(1, width-2))
	maze[initial_height][initial_width] = cell_symbol

	# mark walls around initial cell 
	maze[initial_height-1][initial_width] = wall_symbol
	maze[initial_height][initial_width - 1] = wall_symbol
	maze[initial_height][initial_width + 1] = wall_symbol
	maze[initial_height + 1][initial_width] = wall_symbol

	# add walls around initial cell to wall list
	walls.append([initial_height - 1, initial_width])
	walls.append([initial_height + 1, initial_width])
	walls.append([initial_height, initial_width - 1])
	walls.append([initial_height, initial_width + 1])

	# loop (building process of subsequent paths and walls)
	while (walls):
		wall = walls[(choice(range(0, len(walls))))]

		# check if chosen wall is not left border wall
		if (wall[1] != 0):
			if (maze[wall[0]][wall[1]-1] == unvisited_symbol and maze[wall[0]][wall[1]+1] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on top cell
					if (wall[0] != 0):
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):	
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])


		# check if chosen wall is not top border wall
		if (wall[0] != 0):
			if (maze[wall[0]-1][wall[1]] == unvisited_symbol and maze[wall[0]+1][wall[1]] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on top cell
					if (wall[0] != 0):
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

		# check if chosen wall is not bottom border wall
		if (wall[0] != height-1):
			if (maze[wall[0]+1][wall[1]] == unvisited_symbol and maze[wall[0]-1][wall[1]] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

					# make wall on left cell
					if (wall[1] != 0):
						if (maze[wall[0]][wall[1]-1] != cell_symbol):
							maze[wall[0]][wall[1]-1] = wall_symbol
						if ([wall[0], wall[1]-1] not in walls):
							walls.append([wall[0], wall[1]-1])

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

		# check if chosen wall is not right border wall
		if (wall[1] != width-1):
			if (maze[wall[0]][wall[1]+1] == unvisited_symbol and maze[wall[0]][wall[1]-1] == cell_symbol):
				if (surroundingCells(maze, wall, cell_symbol) < 2):
					# make new cell
					maze[wall[0]][wall[1]] = cell_symbol

					# make wall on right cell
					if (wall[1] != width-1):
						if (maze[wall[0]][wall[1]+1] != cell_symbol):
							maze[wall[0]][wall[1]+1] = wall_symbol
						if ([wall[0], wall[1]+1] not in walls):
							walls.append([wall[0], wall[1]+1])

					# make wall on top cell
					if (wall[0] != 0):	
						if (maze[wall[0]-1][wall[1]] != cell_symbol):
							maze[wall[0]-1][wall[1]] = wall_symbol
						if ([wall[0]-1, wall[1]] not in walls):
							walls.append([wall[0]-1, wall[1]])

					# make wall on bottom cell
					if (wall[0] != height-1):
						if (maze[wall[0]+1][wall[1]] != cell_symbol):
							maze[wall[0]+1][wall[1]] = wall_symbol
						if ([wall[0]+1, wall[1]] not in walls):
							walls.append([wall[0]+1, wall[1]])

		# remove wall from list of walls
		for w in walls:
			if (w[0] == wall[0] and w[1] == wall[1]):
				walls.remove(w)
		
	# mark remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == unvisited_symbol):
				maze[i][j] = wall_symbol

	# mark player starting position
	for i in range(0, width):
		if (maze[1][i] == cell_symbol):
			maze[1][i] = 'P'
			player_position = [1, i]
			break

	# mark level exit position
	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == cell_symbol):
			maze[height-2][i] = 'E'
			break

	# mark random positions of guards, outside of starting safe zone
	guard=0
	while guard in range(guards):
		y = choice(range(1, height-2))
		x = choice(range(1, width-2))
		if (maze[y][x] != wall_symbol):
			guard_position = [y, x]
			if initial_guard_distance(player_position, guard_position):
				maze[y][x] = 'G'
				guard += 1

	# mark random positions of treasures
	treasure=0
	while treasure in range(treasures):
		y = choice(range(1, height-2))
		x = choice(range(1, width-2))
		if (maze[y][x] != wall_symbol):
			if ((maze[y-1][x] or maze[y+1][x] or maze[y][x-1] or maze[y][x+1]) != 'G'):
				maze[y][x] = 'T'
				treasure += 1

	save_generated_level(maze)