with open("input2.txt") as f:
    content = f.readlines()

program = list(map(int,  content[0].split(",")))

program[1] = 12
program[2] = 2

cur_pos = 0
op_code = program[cur_pos]

while op_code != 99:
    if op_code == 1:
        program[program[cur_pos + 3]] = program[program[cur_pos + 1]] + program[program[cur_pos + 2]]
        cur_pos = cur_pos + 4
        op_code = program[cur_pos]
    else:
        if op_code == 2:
            program[program[cur_pos + 3]] = program[program[cur_pos + 1]] * program[program[cur_pos + 2]]
            cur_pos = cur_pos + 4
            op_code = program[cur_pos]
        else:
            print ("something is broken")
            print(op_code)
            print(cur_pos)
            exit(0)

print("part 1 = " + str(program[0]))
