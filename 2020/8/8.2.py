with open("input8.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
commands = []
global_acc = 0

for cur_line in content:
    command_str = cur_line.split(' ')
    command_name = command_str[0]
    commands.append([command_name, int(command_str[1].strip())])

changed_command = 0
while changed_command in range(len(commands)):
    global_acc = 0
    ip = 0
    visited_ips = []
    while ip in range(len(commands)):
        cur_command = commands[ip][0]
        if ip == changed_command:
            if cur_command == "nop":
                cur_command = "jmp"
            else:
                if cur_command == "jmp":
                    cur_command = "nop"

        if ip in visited_ips:
            break
        visited_ips.append(ip)
        if cur_command == "jmp":
            ip += commands[ip][1]
            continue
        if cur_command == "acc":
            global_acc += commands[ip][1]
        ip = ip + 1

    if ip == len(commands):
        part2 = global_acc
        break
    changed_command += 1

print("part 2 = " + str(part2))