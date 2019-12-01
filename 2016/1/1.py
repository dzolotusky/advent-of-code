with open("input1.txt") as f:
    content = f.readlines()

directions = content[0].split(", ")

cur_loc = 0
cur_dir = 1
part2 = None

visited = [0]

for dir in directions:
    if dir[0] == 'R':
        cur_dir *= 1j
    else:
        if dir[0] == 'L':
            cur_dir /= 1j

    steps = int(dir[1:])
    for step in range(steps):
        cur_loc += cur_dir

        if cur_loc in visited and part2 is None:
            part2 = cur_loc

        visited.append(cur_loc)

print("part 1 = " + str(int(abs(cur_loc.real) + abs(cur_loc.imag))))

if part2 is not None:
    print("part 2 = " + str(int(abs(part2.real) + abs(part2.imag))))
