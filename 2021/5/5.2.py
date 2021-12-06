with open("input5.txt") as f:
    content = f.readlines()

covered = {}


def add_covered(x, y):
    if (x, y) in covered:
        covered[(x, y)] += 1
    else:
        covered[(x, y)] = 1


for cur_line in content:
    cur_line_split = cur_line.split(" -> ")
    start_coords = cur_line_split[0].split(",")
    end_coords = cur_line_split[1].split(",")
    start_coords = [int(n) for n in start_coords]
    end_coords = [int(n) for n in end_coords]

    if start_coords[0] == end_coords[0]:
        stepx = 0
    else:
        if start_coords[0] < end_coords[0]:
            stepx = 1
        else:
            stepx = -1

    if start_coords[1] == end_coords[1]:
        stepy = 0
    else:
        if start_coords[1] < end_coords[1]:
            stepy = 1
        else:
            stepy = -1

    cur_coord = [start_coords[0], start_coords[1]]
    while cur_coord != end_coords:
        add_covered(cur_coord[0], cur_coord[1])
        cur_coord = [cur_coord[0] + stepx, cur_coord[1] + stepy]
    add_covered(end_coords[0], end_coords[1])

part2 = 0
for point in covered:
    if covered[point] > 1:
        part2 += 1

print("part 2 = " + str(part2))