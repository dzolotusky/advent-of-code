with open("input9.txt") as f:
    content = f.readlines()

part2 = 0

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


low_points = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_low_point(i, j):
            low_points.append((i, j))


visited = []


def find_size(cur_point):
    if cur_point[0] < 0:
        return 0
    if cur_point[0] > len(grid) - 1:
        return 0
    if cur_point[1] < 0:
        return 0
    if cur_point[1] > len(grid[cur_point[0]]) - 1:
        return 0

    if cur_point in visited:
        return 0
    if grid[cur_point[0]][cur_point[1]] == 9:
        visited.append(cur_point)
        return 0
    visited.append(cur_point)
    return 1 + find_size((cur_point[0] - 1, cur_point[1])) + find_size((cur_point[0] + 1, cur_point[1])) + find_size((cur_point[0], cur_point[1] - 1)) + find_size((cur_point[0], cur_point[1] + 1))


basin_sizes = []
for low_point in low_points:
    visited = []
    size = find_size(low_point)
    basin_sizes.append(size)

basin_sizes.sort()
part2 = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

print("part 2 = " + str(part2))
