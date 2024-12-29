with open("test_input22.txt") as f:
    content = f.readlines()

part2 = 0
ranges = []
cubes = {}

for cur_line in content:
    cur_line_split = cur_line.strip().split(",")
    x_split = cur_line_split[0].split()
    x_range = [int(n) for n in x_split[1][2:].split("..")]
    y_range = [int(n) for n in cur_line_split[1][2:].split("..")]
    z_split = cur_line_split[2].split()
    z_range = [int(n) for n in cur_line_split[2][2:].split("..")]

    # if x_range[0] >= x_range[1]:
    #     print("x")
    # if y_range[0] >= y_range[1]:
    #     print("y")
    # if z_range[0] >= z_range[1]:
    #     print("z")
    #   below is for part 1
    #    if x_range[0] < -50 or x_range[1] > 50 or y_range[0] < -50 or y_range[1] > 50 or z_range[0] < -50 or z_range[1] > 50:
    #        continue
    ranges.append((1 if x_split[0] == "on" else 0, (x_range, y_range, z_range)))

overlaps = [0] * len(ranges)
for outer_range_index, outer_range in enumerate(ranges):
    for inner_range_index, inner_range in enumerate(ranges):
        if inner_range_index >= outer_range_index:
            continue

        outer_xs = outer_range[1][0]
        outer_ys = outer_range[1][1]
        outer_zs = outer_range[1][2]

        inner_xs = inner_range[1][0]
        inner_ys = inner_range[1][1]
        inner_zs = inner_range[1][2]

        total_overlap = 0
        if (outer_xs[0] <= inner_xs[0] <= outer_xs[1] or outer_xs[0] <= inner_xs[1] <= outer_xs[1]) and \
                (outer_ys[0] <= inner_ys[0] <= outer_ys[1] or outer_ys[0] <= inner_ys[1] <= outer_ys[1]) and \
                (outer_zs[0] <= inner_zs[0] <= outer_zs[1] or outer_zs[0] <= inner_zs[1] <= outer_zs[1]):
            # print("overlap: " + str((outer_range_index, inner_range_index)))
            # if outer_range_index <= inner_range_index:
            #    print("crap")
#DZOLO: figure out how to calculate cube overlaps
            overlap_x = 0
            for cur_x in range(outer_xs[0], outer_xs[1]):
                if inner_xs[0] < cur_x < inner_xs[1]:
                    overlap_x += 1
            overlap_y = 0
            for cur_y in range(outer_ys[0], outer_ys[1]):
                if inner_ys[0] < cur_y < inner_ys[1]:
                    overlap_y += 1
            overlap_z = 0
            for cur_z in range(outer_zs[0], outer_zs[1]):
                if inner_zs[0] < cur_z < inner_zs[1]:
                    overlap_z += 1
            total_overlap = overlap_x * overlap_y * overlap_z

            # print("overlap: " + str((outer_range_index, inner_range_index, total_overlap)))
            overlaps[inner_range_index] += total_overlap

total_on = 0
for range_index, cur_range in enumerate(ranges):
    if cur_range[0] == 1:
        total_on += (cur_range[1][0][1] - cur_range[1][0][0]) * \
                    (cur_range[1][1][1] - cur_range[1][1][0]) * \
                    (cur_range[1][2][1] - cur_range[1][2][0])
        total_on -= overlaps[range_index]

part2 = total_on
print("part 2 = " + str(part2))
