with open("input10.txt") as f:
    content = f.readlines()

part1 = 0
cur_cycle = 1
register = 1
commands = []

for cur_line in content:
    command_split = cur_line.strip().split(' ')
    if len(command_split) > 1:
        command_split[1] = int(command_split[1])
    commands.append(command_split)

ip = 0
while ip in range(len(commands)):
    if cur_cycle % 20 == 0 and (cur_cycle / 20) % 2 == 1:
        part1 += cur_cycle * register

    if (cur_cycle + 1) % 20 == 0 and ((cur_cycle + 1) / 20) % 2 == 1 and commands[ip][0] == "addx":
        part1 += (cur_cycle + 1) * register

    if commands[ip][0] == "addx":
        register += commands[ip][1]
        cur_cycle += 1

    if commands[ip][0] == "noop":
        ip = ip

    cur_cycle += 1
    ip = ip + 1

print("part1 = " + str(part1))
