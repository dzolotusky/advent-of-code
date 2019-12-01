with open("input8.txt") as f:
    content = f.readlines()

grid = []

for i in range(0, 6):
    sub_array = ['.'] * 50
    grid.append(sub_array)


def print_grid():
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


for cur_line_index, cur_line in enumerate(content):
    print_grid()
    cur_line_split = cur_line.split(' ')
    if cur_line_split[0] == 'rect':
        rect = [int(val) for val in cur_line_split[1].split('x')]
        for i in range(rect[1]):
            for j in range(rect[0]):
                grid[i][j] = '#'
    else:
        shift_size = int(cur_line_split[-1].strip())
        shift_loc = int(cur_line_split[2][cur_line_split[2].index('=') + 1:])
        if cur_line_split[1] == "row":
            shift_size %= len(grid[0])
            new_row = []
            new_row[:shift_size] = grid[shift_loc][-shift_size:]
            new_row[shift_size:] = grid[shift_loc][:-shift_size]
            grid[shift_loc] = new_row
        else:
            shift_size %= len(grid)
            new_col = [None] * len(grid)
            for i in range(len(grid)):
                new_col[(i + shift_size) % len(grid)] = grid[i][shift_loc]

            for i in range(len(grid)):
                grid[i][shift_loc] = new_col[i]

print_grid()

lights_on = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            lights_on += 1

print("part 1 = " + str(lights_on))
