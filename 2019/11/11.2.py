with open("input11.txt") as f:
    content = f.readlines()

grid = []
for i in range(8):
    sub_array = ['.'] * 50
    grid.append(sub_array)


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


location = (0,0)
direction = (-1,0)
painted = []
relative_base = 0
output_type = 0
grid[0][0] = '#' # for part 2

def getInput():
    return 0 if grid[location[0]][location[1]] == '.' else 1


def processOutput(output_val):
    global output_type
    global direction
    global location

    if output_type == 0:
        grid[location[0]][location[1]] = '.' if output_val == 0 else '#'
        painted.append((location[0],location[1]))
    else:
        if output_val == 0: #left
            if direction == (-1,0):
                direction = (0,-1)
            else:
                if direction == (1,0):
                    direction = (0,1)
                else:
                    if direction == (0,-1):
                        direction = (1, 0)
                    else:
                        if direction == (0,1):
                            direction = (-1, 0)
        if output_val == 1: #right
            if direction == (-1,0):
                direction = (0,1)
            else:
                if direction == (1,0):
                    direction = (0,-1)
                else:
                    if direction == (0,-1):
                        direction = (-1, 0)
                    else:
                        if direction == (0,1):
                            direction = (1, 0)

        location = (location[0] + direction[0], location[1] + direction[1])

    output_type += 1
    output_type %= 2


def do_line(pos, ins, mem, p1_mode, p2_mode, p3_mode):
    global relative_base
    #    if p1_mode == 2 or p2_mode == 2:
    #        print("mode 2")
    p1 = mem[mem[pos + 1]] if p1_mode == 0 else mem[pos + 1] if p1_mode == 1 else mem[mem[pos + 1] + relative_base]
    if ins < 3 or 9 > ins > 4:
        p2 = mem[mem[pos + 2]] if p2_mode == 0 else mem[pos + 2] if p2_mode == 1 else mem[mem[pos + 2] + relative_base]
    p3_loc = mem[pos + 3] if p3_mode == 0 else pos + 3 if p3_mode == 1 else mem[pos + 3] + relative_base

    if ins == 1:
        mem[p3_loc] = p1 + p2
        # print("1: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
        pos = pos + 4
    else:
        if ins == 2:
            mem[p3_loc] = p1 * p2
            # print("2: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
            pos = pos + 4
        else:
            if ins == 3:
                input_param = getInput()
                if p1_mode == 2:
                    mem[mem[pos + 1] + relative_base] = input_param
                else:
                    mem[mem[pos + 1]] = input_param
                # print("3: " + str(mem[pos + 1]) + " " + str(input_param))
                print("used input param " + str(input_param))
                pos = pos + 2
            else:
                if ins == 4:
                    output_param = p1
                    # print("4: " + str(p1) + " " + str(output_param))
                    print("output = " + str(output_param))
                    pos = pos + 2
                    processOutput(output_param)
                else:
                    if ins == 5:
                        if not p1 == 0:
                            pos = p2
                        else:
                            pos = pos + 3
                        # print("5: " + str(p1) + " " + str(p2))
                    else:
                        if ins == 6:
                            if p1 == 0:
                                pos = p2
                            else:
                                pos = pos + 3
                            # print("6: " + str(p1) + " " + str(p2))
                        else:
                            if ins == 7:
                                # print("7: " + str(p1) + " " + str(p2) + " " + str(mem[pos + 3]))
                                if p1 < p2:
                                    mem[p3_loc] = 1
                                else:
                                    mem[p3_loc] = 0
                                pos = pos + 4
                            else:
                                if ins == 8:
                                    # print("8: " + str(p1) + " " + str(p2) + " " + str(mem[pos + 3]))
                                    if p1 == p2:
                                        mem[p3_loc] = 1
                                    else:
                                        mem[p3_loc] = 0

                                    pos = pos + 4
                                else:
                                    if ins == 9:
                                        relative_base += p1
                                        pos = pos + 2
                                    else:
                                        print("something is broken")
                                        print("ins = " + str(ins))
                                        print("pos = " + str(pos))
                                        print("full state = " + str(mem))
                                        exit(0)
    ins = program[pos]
    #    print("full state = " + str(mem))
    return pos, ins, mem


program = list(map(int, content[0].split(","))) + [0] * 10000
cur_pos = 0
op_code = program[cur_pos]

while op_code % 100 != 99:
    ins = op_code % 100
    p1_mode = 0
    p2_mode = 0
    p3_mode = 0

    if op_code > 100:
        p1_mode = int(op_code / 100) % 10
    if op_code > 1000:
        p2_mode = int(op_code / 1000) % 10
    if op_code > 10000:
        p3_mode = int(op_code / 10000) % 10

    cur_pos, op_code, program = do_line(cur_pos, ins, program, p1_mode, p2_mode, p3_mode)

print_grid()
print(painted)
print(len(painted))
print(len(set(painted)))