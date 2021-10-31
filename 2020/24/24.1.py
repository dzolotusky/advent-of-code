with open("input24.txt") as f:
    content = f.readlines()

part1 = 0
tile_flips = {}

for cur_line in content:
    cur_line = cur_line.strip()
    line_index = 0
    cur_coord = [0,0]
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
    if cur_coord not in tile_flips:
        tile_flips[cur_coord] = 0

    tile_flips[cur_coord] += 1

for flips in tile_flips:
    if tile_flips[flips] == 1:
        part1 += 1

print("part 1 = " + str(part1))