with open("input25.txt") as f:
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

step_count = 0
changes = True
while changes:
    step_count += 1
    changes = False
    new_grid = []
    for i in range(len(grid)):
        sub_array = ['.'] * len(grid[0])
        new_grid.append(sub_array)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '>':
                new_j = (j + 1) % len(grid[i])
                if grid[i][new_j] == '.':
                    new_grid[i][new_j] = '>'
                    changes = True
                else:
                    new_grid[i][j] = '>'
            if grid[i][j] == 'v':
                new_grid[i][j] = 'v'
    grid = new_grid.copy()

    new_grid = []
    for i in range(len(grid)):
        sub_array = ['.'] * len(grid[0])
        new_grid.append(sub_array)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'v':
                new_i = (i + 1) % len(grid)
                if grid[new_i][j] == '.':
                    new_grid[new_i][j] = 'v'
                    changes = True
                else:
                    new_grid[i][j] = 'v'
            if grid[i][j] == '>':
                new_grid[i][j] = '>'
    grid = new_grid

part1 = step_count
print("part 1 = " + str(part1))
