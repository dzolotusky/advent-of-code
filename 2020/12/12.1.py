with open("input12.txt") as f:
    content = f.readlines()

part1 = 0

loc = (0, 0)
dir_idx = 0
directions = [(1,0), (0,-1), (-1,0), (0,1)]

for step in content:
    ins = step[0]
    num = int(step[1:])
    if ins == "F":
        new_loc = (loc[0] + num * directions[dir_idx][0], loc[1] +  num * directions[dir_idx][1])
        loc = new_loc
    if ins == "N":
        new_loc = (loc[0], loc[1] + num)
        loc = new_loc
    if ins == "S":
        new_loc = (loc[0], loc[1] - num)
        loc = new_loc
    if ins == "E":
        new_loc = (loc[0] + num, loc[1])
        loc = new_loc
    if ins == "W":
        new_loc = (loc[0] - num, loc[1])
        loc = new_loc
    if ins == "R":
        num /= 90
        dir_idx += int(num)
        dir_idx %= 4
    if ins == "L":
        num /= 90
        dir_idx -= int(num)
        dir_idx %= 4

part1 = abs(loc[0]) + abs(loc[1])
print("part 1 = " + str(part1))