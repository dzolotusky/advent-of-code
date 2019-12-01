from collections import deque

#input = 10
#target = (4, 7)

input = 1364
target = (39, 31)

grid = []
for i in range(0, target[0] + 100):
    sub_array = ['.'] * (target[1] + 100)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        val = j * j + 3 * j + 2 * j * i + i + i * i
        val += input
        ones = bin(val).count('1')
        if ones % 2 == 0:
            grid[i][j] = '.'
        else:
            grid[i][j] = '#'


def print_grid(grid_to_print):
    for i in range(len(grid_to_print)):
        for j in range(len(grid_to_print[i])):
            print(grid_to_print[i][j], end='')
        print('')


def shortest_path(loc1, loc2):
    if dist(loc1, loc2) == 1:
        return loc2, 1

    queue = deque([])
    cur_loc = loc1
    visited = {}
    queue.append((cur_loc, 0, []))
    while len(queue) > 0:
        cur_loc, distance, path = queue.popleft()
        if cur_loc not in visited:
            if cur_loc == loc2:
                return path[1], distance
            if len(visited) == 0 or grid[cur_loc[0]][cur_loc[1]] == '.' or grid[cur_loc[0]][cur_loc[1]] != '#':
                if (cur_loc[0] - 1, cur_loc[1]) not in visited:
                    queue.append(((cur_loc[0] - 1, cur_loc[1]), distance + 1, path + [cur_loc]))
                if (cur_loc[0], cur_loc[1] - 1) not in visited:
                    queue.append(((cur_loc[0], cur_loc[1] - 1), distance + 1, path + [cur_loc]))
                if (cur_loc[0], cur_loc[1] + 1) not in visited:
                    queue.append(((cur_loc[0], cur_loc[1] + 1), distance + 1, path + [cur_loc]))
                if (cur_loc[0] + 1, cur_loc[1]) not in visited:
                    queue.append(((cur_loc[0] + 1, cur_loc[1]), distance + 1, path + [cur_loc]))
            visited[cur_loc] = distance, path + [cur_loc]

    return None


def dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

print(shortest_path((1,1), target)[1])