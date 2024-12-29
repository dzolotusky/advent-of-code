with open("input10.txt") as f:
    content = f.readlines()

cur_cycle = 1
register = 1
commands = []
grid = []
values = []


def print_grid():
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


for i in range(0, 6):
    sub_array = ['.'] * 40
    grid.append(sub_array)


for cur_line in content:
    command_split = cur_line.strip().split(' ')
    if len(command_split) > 1:
        command_split[1] = int(command_split[1])
    commands.append(command_split)

ip = 0
while ip in range(len(commands)):
    values.append(register)
    if commands[ip][0] == "addx":
        values.append(register)
        register += commands[ip][1]
        cur_cycle += 1

    if commands[ip][0] == "noop":
        ip = ip

    cur_cycle += 1
    ip = ip + 1

values.append(register)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        reg_value = values[i * 40 + j]
        if reg_value - 1 <= j <= reg_value + 1:
            grid[i][j] = '#'
print_grid()

#RFKZCPEF