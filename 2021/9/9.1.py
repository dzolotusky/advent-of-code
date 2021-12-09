with open("input9.txt") as f:
    content = f.readlines()

part1 = 0

grid = []

for cur_line in content:
    cur_line = cur_line.strip()
    cur_line_grid = ['x'] * len(cur_line)
    for i in range(len(cur_line)):
        cur_line_grid[i] = int(cur_line[i])
    grid.append(cur_line_grid)


def is_low_point(i, j):
    cur_val = grid[i][j]
    if i > 0 and grid[i - 1][j] <= cur_val:
        return False
    if i < len(grid) - 1 and grid[i + 1][j] <= cur_val:
        return False
    if j > 0 and grid[i][j - 1] <= cur_val:
        return False
    if j < len(grid[i]) - 1 and grid[i][j + 1] <= cur_val:
        return False
    return True


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_low_point(i, j):
            part1 += grid[i][j] + 1

print("part 1 = " + str(part1))
