with open("input2.txt") as f:
    content = f.readlines()


def do_line(pos, ins, mem):
    if ins == 1:
        mem[mem[pos + 3]] = mem[mem[pos + 1]] + mem[mem[pos + 2]]
    else:
        if ins == 2:
            mem[mem[pos + 3]] = mem[mem[pos + 1]] * mem[mem[pos + 2]]
        else:
            print("something is broken")
            print("n = " + str(n))
            print("v = " + str(v))
            print("ins = " + str(ins))
            print("pos = " + str(pos))
            print("full state = " + str(mem))
            exit(0)

    pos = pos + 4
    ins = program[pos]
    return pos, ins, mem


n = -1
v = -1
while n < 99:
    n = n + 1
    v = -1
    while v < 99:
        v = v + 1
        program = list(map(int, content[0].split(",")))
        program[1] = n
        program[2] = v

        cur_pos = 0
        op_code = program[cur_pos]

        while op_code != 99:
            cur_pos, op_code, program = do_line(cur_pos, op_code, program)

        if program[0] == 19690720:
            print("answer final state = " + str(program))
            print("n = " + str(n))
            print("v = " + str(v))
            print ("part 2 = " + str(n * 100 + v))
            exit(0)
