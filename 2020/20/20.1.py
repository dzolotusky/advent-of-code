with open("input20.txt") as f:
    content = f.readlines()

part1 = 1
tiles = {}

line_num = 0
while line_num < len(content):
    cur_line = content[line_num]
    if cur_line[0] == "T":
        tile_num = int(cur_line[4:-2])

        line_num += 1
        cur_line = content[line_num]

        grid = []

        while cur_line[0] != '\n':
            sub_array = ['.'] * (len(cur_line) - 1)
            for i in range(len(cur_line) - 1):
                    sub_array[i] = cur_line[i]
            grid.append(sub_array)

            tiles[tile_num] = grid

            line_num += 1
            if line_num < len(content):
                cur_line = content[line_num]
            else:
                break

        line_num += 1

tile_matches = {}
tile_match_numbers = {}
# find the corner grids (ones that only have matches on 2 sides)
for tile_num in tiles:
    tile_grid = tiles[tile_num]
    top = tile_grid[0]
    bottom = tile_grid[-1]
    left = []
    right = []
    for row in range(len(tile_grid)):
        left.append(tile_grid[row][0])
        right.append(tile_grid[row][-1])
    match_num = 0

    for match_tile_num in tiles:
        if match_tile_num == tile_num:
            continue

        match_tile_grid = tiles[match_tile_num]
        match_top = match_tile_grid[0]
        match_bottom = match_tile_grid[-1]

        match_left = []
        match_right = []
        for match_row in range(len(match_tile_grid)):
            match_left.append(match_tile_grid[match_row][0])
            match_right.append(match_tile_grid[match_row][-1])

        if match_bottom == bottom or match_bottom == top or match_bottom == left or match_bottom == right:
            match_num += 1
            continue

        if match_top == bottom or match_top == top or match_top == left or match_top == right:
            match_num += 1
            continue

        if match_left == bottom or match_left == top or match_left == left or match_left == right:
            match_num += 1
            continue

        if match_right == bottom or match_right == top or match_right == left or match_right == right:
            match_num += 1
            continue

        # now reverse
        match_bottom = match_bottom.copy()
        match_top = match_top.copy()
        match_left = match_left.copy()
        match_right = match_right.copy()

        match_bottom.reverse()
        match_top.reverse()
        match_left.reverse()
        match_right.reverse()

        if match_bottom == bottom or match_bottom == top or match_bottom == left or match_bottom == right:
            match_num += 1
            continue

        if match_top == bottom or match_top == top or match_top == left or match_top == right:
            match_num += 1
            continue

        if match_left == bottom or match_left == top or match_left == left or match_left == right:
            match_num += 1
            continue

        if match_right == bottom or match_right == top or match_right == left or match_right == right:
            match_num += 1
            continue

    tile_matches[tile_num] = match_num

for tile_num in tile_matches:
    num_matching = tile_matches[tile_num]
    if num_matching == 2:
        part1 *= tile_num

print("part 1 = " + str(part1))