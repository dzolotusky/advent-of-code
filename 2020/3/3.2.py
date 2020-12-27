with open("input3.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0

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


for indx in range(5):
    total_trees = 0
    mov_x = (1, 3, 5, 7, 1)
    mov_y = (1, 1, 1, 1, 2)
    loc_x = 0
    loc_y = 0

    while loc_y + 1 < len(grid):
        loc_y += mov_y[indx]
        loc_x += mov_x[indx]
        loc_x %= len(grid[0])
        if grid[loc_y][loc_x] == '#':
            total_trees += 1
    if part2 == 0:
        part2 = total_trees
    else:
        part2 *= total_trees

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
