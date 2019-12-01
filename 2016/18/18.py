with open("input18.txt") as f:
    content = f.readlines()

first_row = content[0].strip()

def print_grid(grid_to_print):
    for i in range(len(grid_to_print)):
        for j in range(len(grid_to_print[i])):
            print("." if grid_to_print[i][j] == 1 else "^", end='')
        print('')

grid = []
for i in range(0, 400000):
    sub_array = ['.'] * (len(first_row))
    grid.append(sub_array)

for i in range(len(first_row)):
    grid[0][i] = 1 if first_row[i] == "." else 0

def get_tile_state(i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
        return 1
    else:
        return grid[i][j]

for cur_row_index in range(1, len(grid)):
    for cur_tile_index in range(len(grid[cur_row_index])):
        if get_tile_state(cur_row_index - 1, cur_tile_index - 1) != get_tile_state(cur_row_index - 1, cur_tile_index + 1):
            grid[cur_row_index][cur_tile_index] = 0
        else:
            grid[cur_row_index][cur_tile_index] = 1

part1 = 0
for i in range(len(grid)):
    part1 += sum(grid[i])

print("part 1 = " + str(part1))