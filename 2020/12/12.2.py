with open("input12.txt") as f:
    content = f.readlines()

part2 = 0

ship_loc = (0, 0)
waypoint_loc = (10, 1)
dir_idx = 0
directions = [(1,1), (1,-1), (-1,-1), (-1,1)]

for step in content:
    ins = step[0]
    num = int(step[1:])
    if ins == "F":
        new_loc = (ship_loc[0] + num * waypoint_loc[0], ship_loc[1] +  num * waypoint_loc[1])
        ship_loc = new_loc
    if ins == "N":
        new_loc = (waypoint_loc[0], waypoint_loc[1] + num)
        waypoint_loc = new_loc
    if ins == "S":
        new_loc = (waypoint_loc[0], waypoint_loc[1] - num)
        waypoint_loc = new_loc
    if ins == "E":
        new_loc = (waypoint_loc[0] + num, waypoint_loc[1])
        waypoint_loc = new_loc
    if ins == "W":
        new_loc = (waypoint_loc[0] - num, waypoint_loc[1])
        waypoint_loc = new_loc
    if ins == "R":
        num /= 90
        num = int(num)
        while num > 0:
            new_loc = (waypoint_loc[1], -1 * waypoint_loc[0])
            waypoint_loc = new_loc
            num -= 1
    if ins == "L":
        num /= 90
        num = int(num)
        while num > 0:
            new_loc = (-1 * waypoint_loc[1], waypoint_loc[0])
            waypoint_loc = new_loc
            num -= 1

part2 = abs(ship_loc[0]) + abs(ship_loc[1])
print("part 2 = " + str(part2))