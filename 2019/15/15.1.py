import random

with open("input15.txt") as f:
    content = f.readlines()
# intcode
relative_base = 0

# puzzle 15
start = (30,30)
cur_x = start[0]
cur_y = start[1]
grid = []

for i in range(60):
    sub_array = ['*'] * 60
    grid.append(sub_array)

grid[cur_y][cur_x] = 'S'


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


def get_input():
    global cur_y, cur_x, last_x, last_y
    last_y = cur_y
    last_x = cur_x

    direction = random.randint(1,4)
    if direction == 1:
        cur_y -= 1
    if direction == 2:
        cur_y += 1
    if direction == 3:
        cur_x -= 1
    if direction == 4:
        cur_x += 1
    return direction


def process_output(output_val):
    global cur_y, cur_x, last_x, last_y
    if output_val == 0:
        grid[cur_y][cur_x] = '#'
        cur_y = last_y
        cur_x = last_x
    if output_val == 1:
        if grid[cur_y][cur_x] != 'S':
            grid[cur_y][cur_x] = '.'
    if output_val == 2:
        grid[cur_y][cur_x] = 'X'


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


def walk(pos, cur_dist):
    if pos in visited:
        return
    visited.append(pos)

    cur_dist += 1
    if grid[pos[0]][pos[1]] == 'X':
        print("Part 1 = " + str(cur_dist))
        exit(0)

    if grid[pos[0] + 1][pos[1]] in '.X':
        walk((pos[0] + 1, pos[1]), cur_dist)
    if grid[pos[0] - 1][pos[1]] in '.X':
        walk((pos[0] - 1, pos[1]), cur_dist)
    if grid[pos[0]][pos[1] + 1] in '.X':
        walk((pos[0], pos[1] + 1), cur_dist)
    if grid[pos[0]][pos[1] - 1] in '.X':
        walk((pos[0], pos[1] - 1), cur_dist)

print_grid()

walk(start, -1)
# for part 2, I just read in the map that this generated