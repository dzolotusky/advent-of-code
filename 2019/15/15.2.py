with open("map.txt") as f:
    content = f.readlines()

grid = []
start = (None, None)

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = content[i][j]
        if content[i][j] == 'X':
            start = (i, j)


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


max_dist = 0

visited = []


def walk(pos, cur_dist):
    #grid[pos[0]][pos[1]] = cur_dist % 10
    global max_dist

    if pos in visited:
        return
    visited.append(pos)

    cur_dist += 1
    #print(str(cur_dist) + " : " + str(pos))
    if cur_dist > max_dist:
        max_dist = cur_dist

    if grid[pos[0] + 1][pos[1]] == '.':
        walk((pos[0] + 1, pos[1]), cur_dist)
    if grid[pos[0] - 1][pos[1]] == '.':
        walk((pos[0] - 1, pos[1]), cur_dist)
    if grid[pos[0]][pos[1] + 1] == '.':
        walk((pos[0], pos[1] + 1), cur_dist)
    if grid[pos[0]][pos[1] - 1] == '.':
        walk((pos[0], pos[1] - 1), cur_dist)


walk(start, -1)
#print_grid()
print(str(max_dist))
