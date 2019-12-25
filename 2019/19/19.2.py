from collections import defaultdict

with open("input19.txt") as f:
    content = f.readlines()
# intcode
relative_base = 0

# puzzle 19
grid = []
input_index = -1

for i in range(1800):
    sub_array = ['.'] * 1800
    grid.append(sub_array)


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


def get_input():
    global input_index, cur_y, cur_x
    input_index += 1
    input_index %= 2
    if input_index == 0:
        #print("y = " + str(cur_y))
        return cur_y
    else:
        #print("x = " + str(cur_x))
        return cur_x


def process_output(output_val):
    global grid
    global cur_y, cur_x
    grid[cur_y][cur_x] = '#' if output_val == 1 else '.'
#    if output_val == 1:
#        print(1)
    # print(str((cur_y, cur_x)) + " : " + grid[cur_y][cur_x])


def do_line(pos, ins, mem, p1_mode, p2_mode, p3_mode):
    global relative_base
    #print(pos)
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
                input_param = get_input()
                if p1_mode == 2:
                    mem[mem[pos + 1] + relative_base] = input_param
                else:
                    mem[mem[pos + 1]] = input_param
                # print("3: " + str(mem[pos + 1]) + " " + str(input_param))
                # print("used input param " + str(input_param))
                pos = pos + 2
            else:
                if ins == 4:
                    output_param = p1
                    # print("4: " + str(p1) + " " + str(output_param))
                    # print("output = " + str(output_param))
                    pos = pos + 2
                    process_output(output_param)
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
    return pos, ins


program = list(map(int, content[0].split(",")))
cur_pos = 0
op_code = program[cur_pos]


def default_mem_value():
    return 0


memory = defaultdict(default_mem_value)


def init_memory():
    global memory, program
    memory = defaultdict(default_mem_value)
    for index, value in enumerate(program):
        memory[index] = value


init_memory()
#for cur_y in range(len(grid)):
#    for cur_x in range(len(grid[0])):
cur_y = 1300
cur_x = 0
while cur_y < 1500:
    cur_y += 1
    cur_x = 0
    while cur_x < 1500:
        cur_x += 1
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

            cur_pos, op_code = do_line(cur_pos, ins, memory, p1_mode, p2_mode, p3_mode)

        init_memory()
        cur_pos = 0
        op_code = memory[cur_pos]


totals = {}


def sum_grid():
    for i in range(len(grid) - 99):
        total_in_y = 0
        for j in range(len(grid[i]) - 99):
            if grid[i][j] == '#':
                total_in_y += 1
                if grid[i][j] == '#' and grid[i + 99][j] == '#' and grid[i][j + 99] == '#':
                    print ("Part 2 = " + str((i,j)))
                    exit(0)
        totals[i] = total_in_y

sum_grid()
print(totals)

#print_grid()
# print("Part 1 = " + str(alignment_sum))
