with open("input9.txt") as f:
    content = f.readlines()

head = (0, 0)
tail = (0, 0)
tail_positions = [(0, 0)]


def distance_over_1(first, second):
    return abs(first[0] - second[0]) > 1 or abs(first[1] - second[1]) > 1


def move_head(direction, moves: int):
    global tail, head
    if direction == "U":
        move_delta = [0, 1]
    if direction == "D":
        move_delta = [0, -1]
    if direction == "L":
        move_delta = [-1, 0]
    if direction == "R":
        move_delta = [1, 0]

    for step_num in range(moves):
        old_head = (head[0], head[1])
        head = (head[0] + move_delta[0], head[1] + move_delta[1])
        if distance_over_1(head, tail):
            tail = old_head
            tail_positions.append(old_head)


for cur_line in content:
    cur_line_split = cur_line.split()
    direc = cur_line_split[0]
    steps = int(cur_line_split[1])
    move_head(direc, steps)

part1 = len(set(tail_positions))
print("part1 = " + str(part1))
