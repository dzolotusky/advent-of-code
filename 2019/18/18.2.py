with open("input17.txt") as f:
    content = f.readlines()
# intcode
relative_base = 0

# puzzle 17
grid = []
sub_array = []
Main = ['A', ',', 'C', ',', 'C', ',', 'B', ',', 'A', ',', 'C', ',', 'B', ',', 'A', ',',
        'C', ',', 'B', '\n']
A = ['L', ',', '6', ',', 'R', ',', '1', '2', ',', 'L', ',', '4', ',', 'L', ',', '6', '\n']
B = ['L', ',', '6', ',', 'L', ',', '1', '0', ',', 'L', ',', '1', '0', ',', 'R', ',', '6', '\n']
C = ['R', ',', '6', ',', 'L', ',', '6', ',', 'R', ',', '1', '2', '\n']
video = ['n', '\n']

program_input = Main + A + B + C + video
input_index = -1
part2 = None


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


def get_input():
    global input_index
    input_index += 1
    input = program_input[input_index]
    input = ord(input)
    return input


def process_output(output_val):
    global sub_array, grid, part2
    if input_index > 0:
        part2 = output_val

    if output_val == 10:
        grid.append(sub_array)
        sub_array = []
    else:
        sub_array.append(chr(output_val))


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
    return pos, ins, mem


program = list(map(int, content[0].split(","))) + [0] * 10000
program[0] = 2
cur_pos = 0
op_code = program[cur_pos]

count = 0
while op_code % 100 != 99 and count < 10000000:
    count += 1
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

visited = []
alignment_sum = 0


def walk():
    global alignment_sum
    for cur_y in range(1, len(grid) - 2):
        for cur_x in range(1, len(grid[cur_y]) - 2):
            if grid[cur_y][cur_x] == '#':
                if grid[cur_y + 1][cur_x] == '#' \
                        and grid[cur_y - 1][cur_x] == '#' \
                        and grid[cur_y][cur_x + 1] == '#' \
                        and grid[cur_y][cur_x - 1] == '#':
                    print((cur_y, cur_x))
                    alignment_sum += cur_x * cur_y


#print_grid()
print("Part 2 = " + str(part2))
