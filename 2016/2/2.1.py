with open("input2.txt") as f:
    content = f.readlines()

grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
cur_digit = [1, 1]
code = []


def move(direction):
    if direction == "U":
        cur_digit[0] -= 1
    if direction == "D":
        cur_digit[0] += 1
    if direction == "L":
        cur_digit[1] -= 1
    if direction == "R":
        cur_digit[1] += 1

    for index, val in enumerate(cur_digit):
        if cur_digit[index] < 0:
            cur_digit[index] = 0
        if cur_digit[index] > 2:
            cur_digit[index] = 2


for cur_line in content:
    for direction in cur_line:
        move(direction)

    code.append(grid[cur_digit[0]][cur_digit[1]])

print("".join(code))
