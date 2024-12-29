with open("input9.txt") as f:
    content = f.readlines()

knots = [(0, 0)] * 10
tail_positions = [(0, 0)]


def distance_over_1(first, second):
    return abs(first[0] - second[0]) > 1 or abs(first[1] - second[1]) > 1


def move_head(direction, moves: int):
    global knots
    if direction == "U":
        move_delta = [0, 1]
    if direction == "D":
        move_delta = [0, -1]
    if direction == "L":
        move_delta = [-1, 0]
    if direction == "R":
        move_delta = [1, 0]

    for step_num in range(moves):
        old_knots = knots.copy()
        knots[0] = (knots[0][0] + move_delta[0], knots[0][1] + move_delta[1])
        for knot_num in range(1, len(knots)):
            if distance_over_1(knots[knot_num - 1], knots[knot_num]):
                #                knots[knot_num] = old_knots[knot_num - 1]
                if knots[knot_num][0] < knots[knot_num - 1][0]:
                    knots[knot_num] = (knots[knot_num][0] + 1, knots[knot_num][1])
                if knots[knot_num][0] > knots[knot_num - 1][0]:
                    knots[knot_num] = (knots[knot_num][0] - 1, knots[knot_num][1])
                if knots[knot_num][1] < knots[knot_num - 1][1]:
                    knots[knot_num] = (knots[knot_num][0], knots[knot_num][1] + 1)
                if knots[knot_num][1] > knots[knot_num - 1][1]:
                    knots[knot_num] = (knots[knot_num][0], knots[knot_num][1] - 1)

                if knot_num == 9:
                    tail_positions.append(knots[knot_num])


for cur_line in content:
    cur_line_split = cur_line.split()
    direc = cur_line_split[0]
    steps = int(cur_line_split[1])
    move_head(direc, steps)

part2 = len(set(tail_positions))
print("part2 = " + str(part2))
