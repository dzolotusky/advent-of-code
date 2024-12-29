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

        if inner_range[0] != outer_range[0]:
            continue

        outer_xs = outer_range[1][0]
        outer_ys = outer_range[1][1]
        outer_zs = outer_range[1][2]

        inner_xs = inner_range[1][0]
        inner_ys = inner_range[1][1]
        inner_zs = inner_range[1][2]

        total_overlap = max(min(outer_xs[1],inner_xs[1])-max(outer_xs[0],inner_xs[0]),0) *\
                        max(min(outer_ys[1],inner_ys[1])-max(outer_ys[0],inner_ys[0]),0) *\
                        max(min(outer_zs[1],inner_zs[1])-max(outer_zs[0],inner_zs[0]),0)

        if total_overlap > 0:
            overlaps[inner_range_index] += total_overlap

# total_on = 0
# total_off = 0
# for range_index, cur_range in enumerate(ranges):
#     if cur_range[0] == 1:
#         total_on += (cur_range[1][0][1] - cur_range[1][0][0]) * \
#                     (cur_range[1][1][1] - cur_range[1][1][0]) * \
#                     (cur_range[1][2][1] - cur_range[1][2][0])
#         total_on -= overlaps[range_index]
#
#     if cur_range[0] == 0:
#         total_off += (cur_range[1][0][1] - cur_range[1][0][0]) * \
#                     (cur_range[1][1][1] - cur_range[1][1][0]) * \
#                     (cur_range[1][2][1] - cur_range[1][2][0])
#         total_off -= overlaps[range_index]
#
# part2 = total_on - total_off

for range_index, cur_range in enumerate(ranges):
    print((range_index, cur_range[0], cur_range[1], overlaps[range_index]))
print("part 2 = " + str(part2))
