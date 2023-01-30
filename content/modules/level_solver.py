from content.modules.level_functions import load_level
def random_maze_solver(level_name):

    l = load_level(level_name)
    level = []
    for count_x, x in enumerate(l):
        level.append([])
        for count_y, y in enumerate(l[count_x]):
            if y == 'X':
                level[count_x].append(1)
            elif y == 'P':
                start = [count_x, count_y]
                level[count_x].append(0)
            elif y == 'E':
                exit = [count_x, count_y]
                level[count_x].append(0)
            else: 
                level[count_x].append(0)

    
    def make_step(k):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i>0 and m[i-1][j] == 0 and level[i-1][j] == 0:
                        m[i-1][j] = k + 1
                    if j>0 and m[i][j-1] == 0 and level[i][j-1] == 0:
                        m[i][j-1] = k + 1
                    if i<len(m)-1 and m[i+1][j] == 0 and level[i+1][j] == 0:
                        m[i+1][j] = k + 1
                    if j<len(m[i])-1 and m[i][j+1] == 0 and level[i][j+1] == 0:
                        m[i][j+1] = k + 1

    m = []
    for i in range(len(level)):
        m.append([])
        for j in range(len(level[i])):
            m[-1].append(0)

    i, j = start[0], start[1]
    m[i][j] = 1

    k = 0
    while m[exit[0]][exit[1]] == 0:
        k += 1
        make_step(k)

    i,j = exit[0], exit[1]
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1

    level_list = [list(a) for a in l]
    for a in the_path:
        if level_list[a[0]][a[1]] == " ":
            level_list[a[0]][a[1]] = 'S'
            
    str_level = ""
    for line in level_list:
        str_level += (''.join(line)) + '\n'
    
    file_path = "./content/levels/" + level_name + "_solved.txt" 
    with open(file_path, 'w') as file:
        file.write(str_level[:-1])

