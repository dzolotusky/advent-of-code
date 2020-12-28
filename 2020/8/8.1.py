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

ip = 0
visited_ips = []
while ip in range(len(commands)):
    if ip in visited_ips:
        break
    visited_ips.append(ip)
    if commands[ip][0] == "jmp":
        ip += commands[ip][1]
        continue
    if commands[ip][0] == "acc":
        global_acc += commands[ip][1]
#    if commands[ip][0] == "nop":
    ip = ip + 1
part1 = global_acc
print("part 1 = " + str(part1))
print("part 2 = " + str(part2))