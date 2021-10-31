with open("input24.txt") as f:
    content = f.readlines()

part1 = 0
black_tiles = []

for cur_line in content:
    cur_line = cur_line.strip()
    line_index = 0
    cur_coord = [0, 0]
    while line_index < len(cur_line):
        if cur_line[line_index] == 'e':
            cur_coord[1] += 1
            line_index += 1
            continue
        if cur_line[line_index] == 'w':
            cur_coord[1] -= 1
            line_index += 1
            continue
        if cur_line[line_index] == 'n' and cur_line[line_index + 1] == 'e':
            cur_coord[0] += 1
            cur_coord[1] += 0.5
            line_index += 2
            continue
        if cur_line[line_index] == 'n' and cur_line[line_index + 1] == 'w':
            cur_coord[0] += 1
            cur_coord[1] -= 0.5
            line_index += 2
            continue
        if cur_line[line_index] == 's' and cur_line[line_index + 1] == 'e':
            cur_coord[0] -= 1
            cur_coord[1] += 0.5
            line_index += 2
            continue
        if cur_line[line_index] == 's' and cur_line[line_index + 1] == 'w':
            cur_coord[0] -= 1
            cur_coord[1] -= 0.5
            line_index += 2
            continue

    cur_coord = (cur_coord[0], cur_coord[1])
    if cur_coord in black_tiles:
        black_tiles.remove(cur_coord)
    else:
        black_tiles.append(cur_coord)

part1 = len(black_tiles)
print("part 1 = " + str(part1))


def count_adjacent(tile_coords):
    num_adjacent_black = 0
    adjacent_white = []
    directions = [(0, 1), (0, -1), (1, 0.5), (1, -0.5), (-1, 0.5), (-1, -0.5)]
    for direction in directions:
        adjacent_tile = (tile_coords[0] + direction[0], tile_coords[1] + direction[1])
        if adjacent_tile in black_tiles:
            num_adjacent_black += 1
        else:
            adjacent_white.append(adjacent_tile)
    return (num_adjacent_black, adjacent_white)


for move_num in range(100):
    new_black_tiles = []
    white_adjacent_to_old_black_tiles = []
    for black_tile in black_tiles:
        (adjacent_black_num, adjacent_white) = count_adjacent(black_tile)
        if adjacent_black_num in [1, 2]:
            new_black_tiles.append(black_tile)
        for white_tile in adjacent_white:
            (adjacent_black_num, _) = count_adjacent(white_tile)
            if adjacent_black_num == 2:
                new_black_tiles.append(white_tile)
    new_black_tiles = list(set(new_black_tiles))
    black_tiles = new_black_tiles

part2 = len(black_tiles)
print("part 2 = " + str(part2))
