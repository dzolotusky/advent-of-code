import sys

with open("input17.txt") as f:
    content = f.readlines()

part2 = 0

grid = {}
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == '#':
            grid[(0, 0, i, j)] = 1


def print_grid():
    max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w = find_edges()
    for cur_x in range(min_x, max_x + 1):
        for cur_y in range(min_y, max_y + 1):
            print("z = " + str(cur_x) + ", w = " + str(cur_y))
            for cur_z in range(min_z, max_z + 1):
                for cur_w in range(min_w, max_w + 1):
                    if (cur_x, cur_y, cur_z, cur_w) in grid and grid[(cur_x, cur_y, cur_z, cur_w)] == 1:
                        print("#", end='')
                    else:
                        print(".", end='')
            print()


def find_edges():
    min_x = min_y = min_z = min_w = sys.maxsize
    max_x = max_y = max_z = max_w = sys.maxsize * -1
    for coord in grid:
        if coord[0] < min_x:
            min_x = coord[0]
        if coord[1] < min_y:
            min_y = coord[1]
        if coord[2] < min_z:
            min_z = coord[2]
        if coord[3] < min_w:
            min_w = coord[3]
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
        if coord[2] > max_z:
            max_z = coord[2]
        if coord[3] > max_w:
            max_w = coord[3]
    return max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w


def count_adjacent(coords):
    num_occ = 0
    for i_delta in range(-1, 2):
        for j_delta in range(-1, 2):
            for k_delta in range(-1, 2):
                for l_delta in range(-1, 2):
                    if i_delta == j_delta == k_delta == l_delta == 0:
                        continue
                    test_coord = (coords[0] + i_delta, coords[1] + j_delta, coords[2] + k_delta, coords[3] + l_delta)
                    if test_coord in grid and grid[test_coord] == 1:
                        num_occ += 1

    return num_occ


for iter in range(6):
    new_grid = {}
    max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w = find_edges()
    for cur_x in range(min_x - 1, max_x + 2):
        for cur_y in range(min_y - 1, max_y + 2):
            for cur_z in range(min_z - 1, max_z + 2):
                for cur_w in range(min_w - 1, max_w + 2):
                    adjacent = count_adjacent((cur_x, cur_y, cur_z, cur_w))
                    if (cur_x, cur_y, cur_z, cur_w) in grid and grid[(cur_x, cur_y, cur_z, cur_w)] == 1:
                        if adjacent == 2 or adjacent == 3:
                            new_grid[(cur_x, cur_y, cur_z, cur_w)] = 1
                    else:
                        if adjacent == 3:
                            new_grid[(cur_x, cur_y, cur_z, cur_w)] = 1
    grid = new_grid.copy()

part2 = sum(grid.values())
print("part 2 = " + str(part2))
