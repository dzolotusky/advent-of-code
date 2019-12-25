with open("map.txt") as f:
    content = f.readlines()

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


print_grid()

total_beam = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            total_beam += 1
print("Part 1 = " + str(total_beam))