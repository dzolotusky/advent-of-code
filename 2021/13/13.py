with open("input13.txt") as f:
    content = f.readlines()

part1 = 0
max_x = 0
max_y = 0
dots = []
folds = []

for cur_line in content:
    if "," in cur_line:
        cur_line_split = cur_line.split(",")
        x = int(cur_line_split[0])
        y = int(cur_line_split[1])
        dots.append((x, y))
        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    if "fold along" in cur_line:
        fold_coord = cur_line[11:].strip()
        fold_coord_split = fold_coord.split("=")
        folds.append((fold_coord_split[0], int(fold_coord_split[1])))

grid = []
for i in range(max_y + 1):
    grid_line = ['.'] * (max_x + 1)
    grid.append(grid_line)


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


for dot in dots:
    grid[dot[1]][dot[0]] = '#'

for fold_num, fold in enumerate(folds):
    if fold[0] == "y":  # fold up
        line = fold[1]
        for i, dot in enumerate(dots):
            if dot[1] > line:
                new_y = 2 * line - dot[1]
                grid[new_y][dot[0]] = '#'
                dots[i] = (dot[0], new_y)
        grid = grid[:line]

    if fold[0] == "x":  # fold left
        line = fold[1]
        for i, dot in enumerate(dots):
            if dot[0] > line:
                new_x = 2 * line - dot[0]
                grid[dot[1]][new_x] = '#'
                dots[i] = (new_x, dot[1])
        for i, cur_row in enumerate(grid):
            grid[i] = cur_row[:line]
    if fold_num == 0:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    part1 += 1

print("part 1 = " + str(part1))
print("part 2 = ")
print_grid()
