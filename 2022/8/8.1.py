with open("input8.txt") as f:
    content = f.readlines()

part1 = 0
grid = []

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = int(content[i][j])


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()

# add outer trees
part1 += len(content) * 2 + (len(content[0].strip()) - 2) * 2

inner_visible = []
# left visible
for i in range(1, len(grid) - 1):
    max_height = grid[i][0]
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] > max_height:
            inner_visible.append((i, j))
            max_height = grid[i][j]

# top visible
for j in range(1, len(grid[i]) - 1):
    max_height = grid[0][j]
    for i in range(1, len(grid) - 1):
        if grid[i][j] > max_height:
            inner_visible.append((i, j))
            max_height = grid[i][j]

# right visible
for i in range(1, len(grid) - 1):
    max_height = grid[i][-1]
    for j in range(len(grid[i]) - 2, 0, -1):
        if grid[i][j] > max_height:
            inner_visible.append((i, j))
            max_height = grid[i][j]

# bottom visible
for j in range(1, len(grid[i]) - 1):
    max_height = grid[-1][j]
    for i in range(len(grid) - 1, 1, -1):
        if grid[i][j] > max_height:
            inner_visible.append((i, j))
            max_height = grid[i][j]

part1 += len(set(inner_visible))
print("part1 = " + str(part1))