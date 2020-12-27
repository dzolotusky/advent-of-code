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


mov_x = 3
mov_y = 1
loc_x = 0
loc_y = 0

while loc_y + 1 < len(grid):
    loc_y += mov_y
    loc_x += mov_x
    loc_x %= len(grid[0])
    print(str(loc_y) + "," + str(loc_x))
    if grid[loc_y][loc_x] == '#':
        part1 += 1

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
