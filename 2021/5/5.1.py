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
        cur_coord = start_coords[1]
        if cur_coord < end_coords[1]:
            while cur_coord <= end_coords[1]:
                add_covered(start_coords[0], cur_coord)
                cur_coord += 1
        else:
            if cur_coord > end_coords[1]:
                while cur_coord >= end_coords[1]:
                    add_covered(start_coords[0], cur_coord)
                    cur_coord -= 1

    if start_coords[1] == end_coords[1]:
        cur_coord = start_coords[0]
        if cur_coord < end_coords[0]:
            while cur_coord <= end_coords[0]:
                add_covered(cur_coord, start_coords[1])
                cur_coord += 1
        else:
            if cur_coord > end_coords[0]:
                while cur_coord >= end_coords[0]:
                    add_covered(cur_coord, start_coords[1])
                    cur_coord -= 1

part1 = 0
for point in covered:
    if covered[point] > 1:
        part1 += 1

print("part 1 = " + str(part1))
