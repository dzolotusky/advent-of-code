with open("input22.txt") as f:
    content = f.readlines()

part1 = 0
ranges = []
cubes = {}

for cur_line in content:
    cur_line_split = cur_line.strip().split(",")
    x_split = cur_line_split[0].split()
    x_range = [int(n) for n in x_split[1][2:].split("..")]
    y_range = [int(n) for n in cur_line_split[1][2:].split("..")]
    z_split = cur_line_split[2].split()
    z_range = [int(n) for n in cur_line_split[2][2:].split("..")]
    if x_range[0] < -50 or x_range[1] > 50 or y_range[0] < -50 or y_range[1] > 50 or z_range[0] < -50 or z_range[1] > 50:
        continue
    ranges.append((1 if x_split[0] == "on" else 0, (x_range, y_range, z_range)))

for cur_range in ranges:
    for cur_x in range(cur_range[1][0][0], cur_range[1][0][1] + 1):
        for cur_y in range(cur_range[1][1][0], cur_range[1][1][1] + 1):
            for cur_z in range(cur_range[1][2][0], cur_range[1][2][1] + 1):
                if cur_range[0] == 1:
                    cubes[(cur_x, cur_y, cur_z)] = 1
                else:
                    if (cur_x, cur_y, cur_z) in cubes:
                        del cubes[(cur_x, cur_y, cur_z)]

part1 = len(cubes)
print("part 1 = " + str(part1))