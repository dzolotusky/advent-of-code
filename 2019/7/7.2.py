with open("input7.txt") as f:
    content = f.readlines()

program = [list(map(int, content[0].split(","))), list(map(int, content[0].split(","))),
           list(map(int, content[0].split(","))), list(map(int, content[0].split(","))),
           list(map(int, content[0].split(",")))]

cur_input = 0


# input_param = [4, 0]
# phase = [4,3,2,1,0]
# output = 0

def do_line(pos, ins, mem, p1_mode, p2_mode, input):
    output_val = None
    p1 = mem[mem[pos + 1]] if p1_mode == 0 else mem[pos + 1]
    if ins < 3 or ins > 4:
        p2 = mem[mem[pos + 2]] if p2_mode == 0 else mem[pos + 2]

    if ins == 1:
        mem[mem[pos + 3]] = p1 + p2
        # print("1: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
        pos = pos + 4
    else:
        if ins == 2:
            mem[mem[pos + 3]] = p1 * p2
            # print("2: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
            pos = pos + 4
        else:
            if ins == 3:
                mem[mem[pos + 1]] = input
                # print("3: " + str(mem[pos + 1]) + " " + str(input_param))
                # print("used input param " + str(input) + " " + str(pos))
                pos = pos + 2
            else:
                if ins == 4:
                    output_param = p1
                    # print("4: " + str(p1) + " " + str(output_param))
                    # print("output = " + str(output_param))
                    output_val = output_param
                    pos = pos + 2
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
                                    mem[mem[pos + 3]] = 1
                                else:
                                    mem[mem[pos + 3]] = 0
                                pos = pos + 4
                            else:
                                if ins == 8:
                                    # print("8: " + str(p1) + " " + str(p2) + " " + str(mem[pos + 3]))
                                    if p1 == p2:
                                        mem[mem[pos + 3]] = 1
                                    else:
                                        mem[mem[pos + 3]] = 0

                                    pos = pos + 4
                                else:
                                    print("something is broken")
                                    print("ins = " + str(ins))
                                    print("pos = " + str(pos))
                                    print("full state = " + str(mem))
                                    exit(0)
    ins = mem[pos]
    #    print("full state = " + str(mem))
    return pos, ins, mem, output_val


def run_phase(phase):
    global program
    global cur_input, output
    output = 0
    amp_outputs = [[], [], [], [], [0]]
    amp_state = [None, None, None, None, None]
    while amp_state != [0, 0, 0, 0, 0]:
        for amp_num in range(5):
            # print("Amp " + str(amp_num))

            cur_input = 0
            output = None

            cur_pos = 0
            input_val = phase[amp_num]

            if amp_state[amp_num] is not None and amp_state[amp_num] != 0:
                (cur_pos, ins, p1_mode, p2_mode) = amp_state[amp_num]
                amp_state[amp_num] = None
                input_amp = amp_num - 1
                if input_amp < 0:
                    input_amp = input_amp + 5

                if len(amp_outputs[input_amp]) > 0:
                    input_val = amp_outputs[input_amp].pop()

            op_code = program[amp_num][cur_pos]

            while op_code % 100 != 99:
                ins = op_code % 100
                p1_mode = 0
                p2_mode = 0

                if op_code > 100:
                    p1_mode = int(op_code / 100) % 10
                if op_code > 1000:
                    p2_mode = int(op_code / 1000) % 10

                cur_pos, op_code, program[amp_num], output = do_line(cur_pos, ins, program[amp_num], p1_mode, p2_mode,
                                                                     input_val)

                if output is not None:
                    amp_outputs[amp_num] = [output] + amp_outputs[amp_num]

                if op_code == 3:
                    input_amp = amp_num - 1
                    if input_amp < 0:
                        input_amp = input_amp + 5

                    if len(amp_outputs[input_amp]) > 0:
                        input_val = amp_outputs[input_amp].pop()
                    else:
                        amp_state[amp_num] = (cur_pos, ins, p1_mode, p2_mode)
                        break

            if op_code % 100 == 99:
                amp_state[amp_num] = 0

    return amp_outputs[4][0]


import itertools

# phases = list(itertools.permutations([0, 1, 2, 3, 4]))
phases = list(itertools.permutations([5, 6, 7, 8, 9]))

# print(phases)
# phases = [[9,8,7,6,5]]
# phases = [[9,7,8,5,6]]
max_val = 0
for phase in phases:
    print(phase)
    cur_val = run_phase(phase)
    if cur_val > max_val:
        max_val = cur_val

print("part 2 = " + str(max_val))

# print(run_phase([1,0,4,3,2]))
# print ("final output = " + str(output))
