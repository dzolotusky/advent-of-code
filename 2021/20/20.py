import math

with open("input20.txt") as f:
    content = f.readlines()

part1 = 0

alg = content[0].strip()
min = [math.inf, math.inf]
max = [math.inf * -1, math.inf * -1]
outside_value = 0
grid = {}
for i, cur_line in enumerate(content[2:]):
    cur_line = cur_line.strip()
    for j in range(len(cur_line)):
        if cur_line[j] == '#':
            grid[i, j] = cur_line[j]
            if i < min[0]:
                min[0] = i
            if i > max[0]:
                max[0] = i
            if j < min[1]:
                min[1] = j
            if j > max[1]:
                max[1] = j


def calculate_value(i_loc, j_loc, cur_grid):
    pixels = []
    for cur_i in range(i_loc - 1, i_loc + 2):
        for cur_j in range(j_loc - 1, j_loc + 2):
            if (cur_i, cur_j) in cur_grid:
                pixels.append("1")
            else:
                if cur_i < min[0] or cur_i > max[0] or cur_j < min[1] or cur_j > max[1]:
                    pixels.append(str(outside_value))
                else:
                    pixels.append("0")
    bin_string = "".join(pixels)
    alg_index = int(bin_string, 2)
    return alg[alg_index]


def print_grid(cur_grid):
    print()
    for i in range(min[0], max[0] + 1):
        for j in range(min[1], max[1] + 1):
            if (i,j) in cur_grid:
                print(grid[(i,j)], end='')
            else:
                print('.', end='')
        print()


for enhance_round in range(50):
    if enhance_round == 2:
        part1 = len(grid)
    new_grid = {}
    new_min = (min[0] - 2, min[1] - 2)
    new_max = (max[0] + 2, max[1] + 2)
    for i in range(new_min[0] - 2, new_max[0] + 2):
        for j in range(new_min[1] - 2, new_max[1] + 2):
            new_value = calculate_value(i, j, grid)
            if new_value == '#':
                new_grid[(i,j)] = new_value

    grid = new_grid
    min = new_min
    max = new_max
    if outside_value == 0:
        outside_value = 1 if alg[0] == '#' else 0
    else:
        if outside_value == 1:
            outside_value = 1 if alg[-1] == '#' else 0

    #print_grid(new_grid)
    #print(len(new_grid))

part2 = len(grid)
print("part 1 = " + str(part1))
print("part 2 = " + str(part2))