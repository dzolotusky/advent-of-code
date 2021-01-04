with open("test_input11.txt") as f:
    content = f.readlines()

part1 = 0

grid = []
for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = content[i][j]


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


new_grid = []
for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    new_grid.append(sub_array)


def count_adjacent(test_grid, i, j):
    num_occ = 0
    for i_delta in range(-1, 2):
        if -1 < i + i_delta < len(test_grid):
            for j_delta in range(-1, 2):
                if i_delta == j_delta == 0:
                    continue
                if -1 < j + j_delta < len(test_grid[i]):
                    if test_grid[i+i_delta][j+j_delta] == "#":
                        num_occ += 1
    return num_occ


made_change = True
while made_change:
    new_grid = []
    for i in range(len(content)):
        sub_array = ['.'] * (len(content[0]) - 1)
        new_grid.append(sub_array)

    made_change = False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "L" and count_adjacent(grid, i, j) == 0:
                new_grid[i][j] = "#"
                made_change = True
            else:
                if grid[i][j] == "#" and count_adjacent(grid, i, j) > 3:
                    new_grid[i][j] = "L"
                    made_change = True
                else:
                    new_grid[i][j] = grid[i][j]
    grid = new_grid



for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            part1 += 1

print("part 1 = " + str(part1))