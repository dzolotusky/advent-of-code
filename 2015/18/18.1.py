with open("input18.txt") as f:
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


print("Initial state:")
print_grid()


def get_adjacent_on(cur_i, cur_j):
    adjacent_on = 0
    for i_change in range(-1, 2):
        for j_change in range(-1, 2):
            if i_change == 0 and j_change == 0:
                continue
            new_spot = (cur_i + i_change, cur_j + j_change)
            if new_spot[0] < 0 or new_spot[1] < 0:
                continue
            if new_spot[0] >= len(grid[0]) or new_spot[1] >= len(grid[0]):
                continue
            if grid[new_spot[0]][new_spot[1]] == '#':
                adjacent_on = adjacent_on + 1
    return adjacent_on


def change_square(i, j):
    adj_on = get_adjacent_on(i, j)
    if adj_on == 3:
        return '#'

    if grid[i][j] == '#':
        if adj_on == 2:
            return '#'

    return '.'


for counter in range(100):
    new_grid = []
    for i in range(len(content)):
        sub_array = ['.'] * (len(content[0]) - 1)
        new_grid.append(sub_array)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = change_square(i, j)

    grid = new_grid

#    print("After " + str(counter + 1) + "minutes:")
#    print_grid()

total_on = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            total_on = total_on + 1

print("done")
print_grid()
print("Total on after " + str(counter + 1) + " steps: " + str(total_on))

# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
#
# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
#
# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
#
# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
#
# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
