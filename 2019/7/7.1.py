with open("input7.txt") as f:
    content = f.readlines()

cur_input = 0
#input_param = [4, 0]
#phase = [4,3,2,1,0]
#output = 0

def run_phase(phase):
    global cur_input, output
    output = 0
    for i in range(5):
        print("Amp " + str(i))
        cur_input = 0
        input_param = [phase[i], output]
        output = None

        def do_line(pos, ins, mem, p1_mode, p2_mode):
            global cur_input, output
            p1 = mem[mem[pos + 1]] if p1_mode == 0 else mem[pos + 1]
            if ins < 3 or ins > 4:
                p2 = mem[mem[pos + 2]] if p2_mode == 0 else mem[pos + 2]

            if ins == 1:
                mem[mem[pos + 3]] = p1 + p2
                #print("1: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
                pos = pos + 4
            else:
                if ins == 2:
                    mem[mem[pos + 3]] = p1 * p2
                    #print("2: " + str(mem[mem[pos + 3]]) + " " + str(p1) + " " + str(p2))
                    pos = pos + 4
                else:
                    if ins == 3:
                        mem[mem[pos + 1]] = input_param[cur_input]
                        #print("3: " + str(mem[pos + 1]) + " " + str(input_param))
                        #print("used input param " + str(cur_input + 1) + ":" + str(input_param[cur_input]))
                        cur_input += 1
                        pos = pos + 2
                    else:
                        if ins == 4:
                            output_param = p1
                            #print("4: " + str(p1) + " " + str(output_param))
                            #print("output = " + str(output_param))
                            output = output_param
                            pos = pos + 2
                        else:
                            if ins == 5:
                                if not p1 == 0:
                                    pos = p2
                                else:
                                    pos = pos + 3
                                #print("5: " + str(p1) + " " + str(p2))
                            else:
                                if ins == 6:
                                    if p1 == 0:
                                        pos = p2
                                    else:
                                        pos = pos + 3
                                    #print("6: " + str(p1) + " " + str(p2))
                                else:
                                    if ins == 7:
                                        #print("7: " + str(p1) + " " + str(p2) + " " + str(mem[pos + 3]))
                                        if p1 < p2:
                                            mem[mem[pos + 3]] = 1
                                        else:
                                            mem[mem[pos + 3]] = 0
                                        pos = pos + 4
                                    else:
                                        if ins == 8:
                                            #print("8: " + str(p1) + " " + str(p2) + " " + str(mem[pos + 3]))
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
            ins = program[pos]
        #    print("full state = " + str(mem))
            return pos, ins, mem


        program = list(map(int, content[0].split(",")))
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

            cur_pos, op_code, program = do_line(cur_pos, ins, program, p1_mode, p2_mode)

    return output

import itertools
phases = list(itertools.permutations([0, 1, 2, 3, 4]))

#print(phases)

max_val = 0
for phase in phases:
    cur_val = run_phase(phase)
    if cur_val > max_val:
        max_val = cur_val

print("part 1 = " + str(max_val))

#print(run_phase([1,0,4,3,2]))
#print ("final output = " + str(output))
