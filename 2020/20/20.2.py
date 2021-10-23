test_input = False
blank_spaces = False
with open("input20.txt") as f:
    content = f.readlines()


def print_grid(grid_to_print):
    for j in range(len(grid_to_print[0])):
        print(int(j / 10), end='')
    print()
    for j in range(len(grid_to_print[0])):
        print(j % 10, end='')
    print()

    for i in range(len(grid_to_print)):
        for j in range(len(grid_to_print[i])):
            print(grid_to_print[i][j], end='')
        print()


part1 = 0
part2 = 0
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
    sides = [tile_grid[0], tile_grid[-1]]
    left = []
    right = []
    for row in range(len(tile_grid)):
        left.append(tile_grid[row][0])
        right.append(tile_grid[row][-1])
    sides.append(left)
    sides.append(right)
    match_num = 0
    matches = []

    for match_tile_num in tiles:
        if match_tile_num == tile_num:
            continue

        match_tile_grid = tiles[match_tile_num]
        match_sides = [match_tile_grid[0], match_tile_grid[-1]]

        match_left = []
        match_right = []
        for match_row in range(len(match_tile_grid)):
            match_left.append(match_tile_grid[match_row][0])
            match_right.append(match_tile_grid[match_row][-1])

        match_sides.append(match_left)
        match_sides.append(match_right)

        for side_indx, side in enumerate(sides):
            for match_side_indx, match_side in enumerate(match_sides):
                if side == match_side:
                    match_num += 1
                    matches.append((match_tile_num, 1 + side_indx, 1 + match_side_indx))

        # now reverse
        reverse_match_sides = []
        for match_side in match_sides:
            reverse_match_sides.append(match_side.copy())
        for match_side in reverse_match_sides:
            match_side.reverse()

        for side_indx, side in enumerate(sides):
            for match_side_indx, match_side in enumerate(reverse_match_sides):
                if side == match_side:
                    match_num += 1
                    matches.append((match_tile_num, 1 + side_indx, -1 * (1 + match_side_indx)))

    tile_matches[tile_num] = match_num
    tile_match_numbers[tile_num] = matches

# print(tile_matches)
tile_matches_inverse = {}
for tile_num in tile_matches:
    num_matching = tile_matches[tile_num]
    if num_matching in tile_matches_inverse:
        tile_matches_inverse[num_matching].append(tile_num)
    else:
        tile_matches_inverse[num_matching] = [tile_num]

# print(tile_matches_inverse)
# print(tile_match_numbers)

# for inv in tile_matches_inverse:
#    print(str(inv) + ":" + str(len(tile_matches_inverse[inv])))

part1 = 1
for corner_tile_num in tile_matches_inverse[2]:
    part1 *= corner_tile_num
print("part 1 = " + str(part1))

# grid is 12x12 of 8x8 maps (10x10 with borders removed)
# test is 3x3 of 8x8
full_grid = []
size = 0
if test_input:
    size = 30
else:
    size = 120
if blank_spaces:
    size = int(size * 1.1)  # 1.1 = adding blank spaces between tiles
tile_size = 10

for i in range(size):
    sub_array = [' '] * size
    full_grid.append(sub_array)

first_corner_tile = tile_matches_inverse[2][0]
# print(first_corner_tile)
# print(tile_match_numbers[first_corner_tile])
first_tile_in_row = (first_corner_tile, False)
visited = [first_corner_tile]
cur_tile = tile_match_numbers[first_corner_tile][0]

sideways = False  # this means that the row is currently matching on the top/bottom and not left/right
flipped_row = False  # this means that the top of this row should be the bottom to match with the next row
if cur_tile[2] in [1, 2, -1, -2]:  # make sure that the second tile matches on the left or right
    if cur_tile[1] == 1:
        flipped_row = True
    cur_tile = tile_match_numbers[first_corner_tile][1]
else:
    if tile_match_numbers[first_corner_tile][1][1] == 1:
        flipped_row = True

if blank_spaces:
     full_grid[0][0] = str(first_corner_tile)[0]
     full_grid[0][1] = str(first_corner_tile)[1]
     full_grid[0][2] = str(first_corner_tile)[2]
     full_grid[0][3] = str(first_corner_tile)[3]

# first tile in both inputs matches on the right with no flipping, just lay it down
for i in range(tile_size):
    for j in range(tile_size):
        full_grid[i + (1 if blank_spaces else 0)][j] = tiles[first_corner_tile][(tile_size - 1) - i][j] if flipped_row else \
            tiles[first_corner_tile][i][j]

offset_x = 1 if blank_spaces else 0  # we've done the first tile in the column
offset_y = (1 + tile_size) if blank_spaces else tile_size  # we've done the first tile in the row
while offset_x + tile_size <= len(full_grid):  # loop through the entire column
    while offset_y + tile_size <= len(full_grid[0]):  # loop through the entire row
        print("Tile = " + str(cur_tile) + ", Offset = " + str(offset_y) + ", Flipped row = " + str(flipped_row) + ", sideways = " + str(sideways))
        visited.append(cur_tile[0])

        if blank_spaces:
             full_grid[offset_x - 1][offset_y] = str(cur_tile[0])[0]
             full_grid[offset_x - 1][offset_y + 1] = str(cur_tile[0])[1]
             full_grid[offset_x - 1][offset_y + 2] = str(cur_tile[0])[2]
             full_grid[offset_x - 1][offset_y + 3] = str(cur_tile[0])[3]

        if cur_tile[2] == 3:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][(tile_size - 1) - i][
                        j] if flipped_row else \
                        tiles[cur_tile[0]][i][j]

        if cur_tile[2] == -3:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][i][j] if flipped_row else \
                        tiles[cur_tile[0]][(tile_size - 1) - i][j]

        if cur_tile[2] == 4:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][(tile_size - 1) - i][
                        (tile_size - 1) - j] if flipped_row else tiles[cur_tile[0]][i][(tile_size - 1) - j]

        if cur_tile[2] == -4:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][i][
                        (tile_size - 1) - j] if flipped_row else tiles[cur_tile[0]][(tile_size - 1) - i][
                        (tile_size - 1) - j]

        if cur_tile[2] == 2:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][(tile_size - 1) - j][
                        (tile_size - 1) - i] if flipped_row else tiles[cur_tile[0]][(tile_size - 1) - j][i]

        if cur_tile[2] == -2:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][(tile_size - 1) - j][
                        i] if flipped_row else tiles[cur_tile[0]][(tile_size - 1) - j][(tile_size - 1) - i]

        if cur_tile[2] == 1:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][j][
                        (tile_size - 1) - i] if flipped_row else tiles[cur_tile[0]][j][i]

        if cur_tile[2] == -1:
            for i in range(tile_size):
                for j in range(tile_size):
                    full_grid[i + offset_x][j + offset_y] = tiles[cur_tile[0]][j][i] if flipped_row else \
                    tiles[cur_tile[0]][j][(tile_size - 1) - i]

        if cur_tile[2] < 0:
            flipped_row = not flipped_row

        if (abs(cur_tile[1]) in [3, 4] and abs(cur_tile[2]) in [1, 2]) or (
                abs(cur_tile[1]) in [1, 2] and abs(cur_tile[2]) in [3, 4]):
            sideways = not sideways

            next_tile = None
        for possible_next_tile in tile_match_numbers[cur_tile[0]]:
            if not sideways and possible_next_tile[1] in [3, 4, -3, -4] and possible_next_tile[0] not in visited:
                next_tile = possible_next_tile
            if sideways and possible_next_tile[1] in [1, 2, -1, -2] and possible_next_tile[0] not in visited:
                next_tile = possible_next_tile
        if next_tile is None:
            break
        else:
            cur_tile = next_tile

        offset_y += (1 + tile_size) if blank_spaces else tile_size

    offset_x += (1 + tile_size) if blank_spaces else tile_size
    offset_y = (1 + tile_size) if blank_spaces else tile_size

#    print_grid(full_grid)

    if offset_x + tile_size <= len(full_grid):
        sideways = False  # this means that the row is currently matching on the top/bottom and not left/right
        flipped_row = False  # this means that the top of this row should be the bottom to match with the next row
        print("first tile in row above= " + str(first_tile_in_row))
        print("first tile in row above matches = " + str(tile_match_numbers[first_tile_in_row[0]]))
        unvisited_neighbors_of_above = [tile_num for tile_num in tile_match_numbers[first_tile_in_row[0]] if
                                        tile_num[0] not in visited]
        unvisited_neighbors = [tile_num for tile_num in tile_match_numbers[unvisited_neighbors_of_above[0][0]] if
                               tile_num[0] not in visited]
        cur_tile = unvisited_neighbors_of_above[0]

        if cur_tile[2] in [3, 4, -3, -4]:  # make sure that the next row matches the previous row on the top or bottom
            if len(unvisited_neighbors_of_above) > 1:
                cur_tile = unvisited_neighbors_of_above[1]
            else:
                sideways = True

        if cur_tile[2] in [-2, 2, -4, 4]:
            flipped_row = True

        first_reversed = False
        if cur_tile[2] in [-1, -2] or first_tile_in_row[1]:
            first_reversed = True

        visited.append(cur_tile[0])

        if blank_spaces:
             full_grid[offset_x - 1][0] = str(cur_tile[0])[0]
             full_grid[offset_x - 1][1] = str(cur_tile[0])[1]
             full_grid[offset_x - 1][2] = str(cur_tile[0])[2]
             full_grid[offset_x - 1][3] = str(cur_tile[0])[3]

        # first tile in both inputs matches on the right with no flipping, just lay it down

        for i in range(tile_size):
            for j in range(tile_size):
                if cur_tile[2] == -3:
                    full_grid[i + offset_x][j] = tiles[cur_tile[0]][(tile_size - 1) - j][
                        (tile_size - 1) - i] if flipped_row else tiles[cur_tile[0]][j][i]
                else:
                    if cur_tile[2] == -4:
                        full_grid[i + offset_x][j] = tiles[cur_tile[0]][j][(tile_size - 1) - i] if flipped_row else tiles[cur_tile[0]][j][(tile_size - 1) - i]
                    else:
                        if cur_tile[2] == 4:
                            full_grid[i + offset_x][j] = tiles[cur_tile[0]][j][(tile_size - 1) - i] if flipped_row else tiles[cur_tile[0]][j][(tile_size - 1) - i]
                            first_reversed = False
                        else:
                            if first_reversed:
                                full_grid[i + offset_x][j] = tiles[cur_tile[0]][(tile_size - 1) - i][(tile_size - 1) - j] if flipped_row else tiles[cur_tile[0]][i][(tile_size - 1) - j]
                            else:
                                full_grid[i + offset_x][j] = tiles[cur_tile[0]][(tile_size - 1) - i][j] if flipped_row else tiles[cur_tile[0]][i][j]

        first_tile_in_row = (cur_tile[0], first_reversed)
        cur_tile = unvisited_neighbors[0]
        if len(unvisited_neighbors) > 1:
            if cur_tile[1] in [1, 2, -1, -2] and not sideways or sideways and cur_tile[1] not in [1, 2, -1, -2]:
                cur_tile = unvisited_neighbors[1]

# reset for next row
offset_y = 0
flipped_row = False

# print(first_corner_tile)
# print(second_tile[0])
# print(tile_match_numbers[first_corner_tile])
# print(tile_match_numbers[second_tile[0]])

print_grid(full_grid)

del_indxs = []
del_i = len(full_grid) - 1
while del_i >= 0:
    del_indxs.append(del_i)
    del full_grid[del_i]
    del_i -= 9
    if del_i >= 0:
        del_indxs.append(del_i)
        del full_grid[del_i]
        del_i -= 1

for i in range(len(full_grid)):
    for j in del_indxs:
        del full_grid[i][j]

if not blank_spaces:
    sea_monster_pixels = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
    matches_in_monster = len(sea_monster_pixels)


    def find_sea_monsters(map):
        sea_monsters = []
        for i in range(len(map)):
            for j in range(len(map[0])):
                matches = 0
                for pixel in sea_monster_pixels:
                    if i + pixel[0] < len(map) and j + pixel[1] < len(map[0]) and map[i + pixel[0]][j + pixel[1]] == '#':
                        matches += 1
                    else:
                        break

                if matches == matches_in_monster:
                    sea_monsters.append((i, j))
        return sea_monsters


    new_grid = full_grid.copy()
    for i in range(len(full_grid)):
        new_row = []
        for j in range(len(full_grid[0])):
            new_row.append(full_grid[i][len(full_grid[0]) - j - 1])
        new_grid[i] = new_row
    grids_with_flips = [full_grid.copy(), list(zip(*full_grid[::-1])), new_grid]

    for i in range(3):
        test_grid = grids_with_flips[i]
        monsters = find_sea_monsters(test_grid)
        if len(monsters) > 0:
            break

        for rotation_count in range(4):
            test_grid = list(zip(*test_grid[::-1]))
            monsters = find_sea_monsters(test_grid)

            if len(monsters) > 0:
                break

        if len(monsters) > 0:
            break
    print(monsters)

    for i in range(len(test_grid)):
        new_row = []
        for j in range(len(test_grid[0])):
            if test_grid[i][j] != '#':
                new_row.append(0)
            else:
                new_row.append(1)
        test_grid[i] = new_row

    for monster in monsters:
        for monster_pixel in sea_monster_pixels:
            test_grid[monster[0] + monster_pixel[0]][monster[1] + monster_pixel[1]] = 0

    for i in range(len(test_grid)):
        part2 += sum(test_grid[i])

    print("part 2 = " + str(part2))
