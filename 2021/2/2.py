with open("input2.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0

#part 1
depth = 0
horizontal_pos = 0

#part2
aim = 0
depth2 = 0
horizontal_pos2 = 0

for cur_line in content:
    cur_line_split = cur_line.split(" ")
    dir = cur_line_split[0]
    steps = int(cur_line_split[1])
    if dir == "up":
        depth -= steps
        aim -= steps
        continue
    if dir == "down":
        depth += steps
        aim += steps
        continue
    if dir == "forward":
        horizontal_pos += steps
        horizontal_pos2 += steps
        depth2 += aim * steps
        continue

part1 = depth * horizontal_pos
part2 = depth2 * horizontal_pos2

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
