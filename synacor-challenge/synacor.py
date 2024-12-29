import sys, array, pickle

content = array.array("h")
with open("challenge.bin", "rb") as f:
    content.fromfile(f, 30050)
if sys.byteorder != "little":
    content.byteswap()

pc = 0
debug_flag = False
count_quote = 0

# all numbers are unsigned integers 0..32767 (15-bit)
# all math is modulo 32768; 32758 + 15 => 5
def read_num(num):
    if num < 0:
        num += 2 ** 16
    if num <= 32767:
        return num
    if num <= 32775:
        if num - 32768 == 7:
            print("reading r8")
        return registers[num - 32768]
    raise ValueError("Invalid Number passed " + str(num) + ". At PC: " + str(pc))


def write_num(address, num):
    if num < 0:
        num += 2 ** 16
    num %= 32768
    if address < 0:
        address += 2 ** 16
    if address <= 32767:
        memory[address] = num
    else:
        if address <= 32775:
            registers[address - 32768] = num
        else:
            raise ValueError("Invalid Address passed " + str(address) + ". At PC: " + str(pc))


while pc < 2 ** 15 - 1:
    memory = [0] * (2 ** 15 - 1)  # memory with 15-bit address space storing 16-bit values
    registers = [0] * 8  # eight registers
    stack = []  # an unbounded stack which holds individual 16-bit values
    input_index = 0
    existing_input = ""

    for i in range(len(content)):  # programs are loaded into memory starting at address 0
        memory[i] = content[i]

    while memory[pc] != 0:  # 0 is halt
        ins = memory[pc]
        if debug_flag:
            print(str(ins) + " at " + str(pc) + ": " + str(read_num(memory[pc + 1])) + "," + str(read_num(memory[pc + 2])) + "," + str(read_num(read_num(memory[pc + 3])))
                  + "/" + str(memory[pc + 1]) + "," + str(memory[pc + 2]) + "," + str(memory[pc + 3]) +
                  str(registers))
        if ins == 1:  # set register <a> to the value of <b>
            write_num(memory[pc + 1], read_num(memory[pc + 2]))
            pc += 2
        if ins == 2:  # push <a> onto the stack
            a = read_num(memory[pc + 1])
            stack.append(a)
            pc += 1
        if ins == 3:  # remove the top element from the stack and write it into <a>; empty stack = error
            if len(stack) == 0:
                raise ValueError("Pop called on Empty Stack")
            write_num(memory[pc + 1], stack.pop())
            pc += 1
        if ins == 4:  # set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
            b = read_num(memory[pc + 2])
            c = read_num(memory[pc + 3])
            write_num(memory[pc + 1], 1 if b == c else 0)
            pc += 3
        if ins == 5:  # set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
            b = read_num(memory[pc + 2])
            c = read_num(memory[pc + 3])
            write_num(memory[pc + 1], 1 if b > c else 0)
            pc += 3
        if ins == 6:  # jump to <a>
            pc = read_num(memory[pc + 1]) - 1
        if ins in [7, 8]:  # 7 if <a> is nonzero, jump to <b>, 8 if <a> is zero, jump to <b>
            a = read_num(memory[pc + 1])
            if (a != 0 and ins == 7) or (a == 0 and ins == 8):
                pc = read_num(memory[pc + 2]) - 1
            else:
                pc += 2
        if ins == 9:  # assign into <a> the sum of <b> and <c> (modulo 32768)
            write_num(memory[pc + 1], read_num(memory[pc + 2]) + read_num(memory[pc + 3]))
            pc += 3
        if ins == 10:  # store into <a> the product of <b> and <c> (modulo 32768)
            write_num(memory[pc + 1], read_num(memory[pc + 2]) * read_num(memory[pc + 3]))
            pc += 3
        if ins == 11:  # store into <a> the remainder of <b> divided by <c>
            write_num(memory[pc + 1], read_num(memory[pc + 2]) % read_num(memory[pc + 3]))
            pc += 3
        if ins == 12:  # stores into <a> the bitwise and of <b> and <c>
            b = read_num(memory[pc + 2])
            c = read_num(memory[pc + 3])
            write_num(memory[pc + 1], b & c)
            pc += 3
        if ins == 13:  # stores into <a> the bitwise or of <b> and <c>
            b = read_num(memory[pc + 2])
            c = read_num(memory[pc + 3])
            write_num(memory[pc + 1], b | c)
            pc += 3
        if ins == 14:  # stores 15-bit bitwise inverse of <b> in <a>
            b = read_num(memory[pc + 2])
            write_num(memory[pc + 1], b ^ 2 ** 15 - 1)
            pc += 2
        if ins == 15:  # read memory at address <b> and write it to <a>
            b = memory[read_num(memory[pc + 2])]
            write_num(memory[pc + 1], b)
            pc += 2
        if ins == 16:  # write the value from <b> into memory at address <a>
            a = read_num(memory[pc + 1])
            b = read_num(memory[pc + 2])
            write_num(a, b)
            pc += 2
        if ins == 17:  # write the address of the next instruction to the stack and jump to <a>
            stack.append(pc + 2)
            pc = read_num(memory[pc + 1]) - 1
        if ins == 18:  # remove the top element from the stack and jump to it; empty stack = halt
            if len(stack) > 0:
                pc = stack.pop() - 1
            else:
                break
        if ins == 19:  # write the character represented by ascii code <a> to the terminal
            value = read_num(memory[pc + 1])
            if chr(value) == '"':
                count_quote += 1
                if count_quote == 4:
                    debug_flag = True
            print(chr(value), end='')
            pc += 1
            # read a character from the terminal and write its ascii code to <a>; it can be assumed that
            # once input starts, it will continue until a newline is encountered; this means that you can
        if ins == 20:  # safely read whole lines from the keyboard and trust that they will be fully read
            if input_index >= len(existing_input):
                existing_input = sys.stdin.readline()
                if existing_input.startswith("r8"):
                    split_input = existing_input.split()
                    r8 = int(split_input[1])
                    registers[7] = r8
                if existing_input == "debug\n":
                    debug_flag = not debug_flag
                if existing_input == "save\n":
                    state = [pc, memory, registers, stack]
                    with open("saved-state.bin", "wb") as f:
                        pickle.dump(state, f)
                if existing_input == "load\n":
                    state = [pc, memory, registers, stack]
                    with open("saved-state.bin", "rb") as f:
                        state = pickle.load(f)
                    pc = state[0]
                    memory = state[1]
                    registers = state[2]
                    stack = state[3]
                    continue
                input_index = 0
            value = existing_input[input_index]
            value = ord(value)
            input_index += 1
            write_num(memory[pc + 1], value)
            pc += 1
        if ins not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
            print("Can't do " + str(ins))
            exit()
        pc += 1
    pc += 1
