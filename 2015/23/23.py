with open("input23.txt") as f:
    content = f.readlines()

commands = []

for cur_line in content:
    command_str = cur_line.split(' ')
    command_name = command_str[0]
    command_str[1] = command_str[1].replace("a", "0")
    command_str[1] = command_str[1].replace("b", "1")
    if "," in cur_line:
        commands.append([command_name, int(command_str[1][:-1]), int(command_str[2].strip())])
    else:
        commands.append([command_name, int(command_str[1].strip())])


def hlf(prev_state, command, ip):
    post_state = prev_state
    post_state[command[1]] = int(post_state[command[1]] / 2)
    return post_state, ip


def tpl(prev_state, command, ip):
    post_state = prev_state
    post_state[command[1]] = post_state[command[1]] * 3
    return post_state, ip


def inc(prev_state, command, ip):
    post_state = prev_state
    post_state[command[1]] = post_state[command[1]] + 1
    return post_state, ip


def jmp(prev_state, command, ip):
    return prev_state, ip + command[1]


def jie(prev_state, command, ip):
    if prev_state[command[1]] % 2 == 0:
        return prev_state, ip + command[2]
    else:
        return prev_state, ip + 1


def jio(prev_state, command, ip):
    if prev_state[command[1]] == 1:
        return prev_state, ip + command[2]
    else:
        return prev_state, ip + 1


print(commands)

cur_state = [1, 0]

ip = 0
while ip in range(len(commands)):
    print(str(ip) + ":" + str(commands[ip]) + " " + str(cur_state))
    if commands[ip][0] == "hlf":
        (cur_state, ip) = hlf(cur_state, commands[ip], ip)
    if commands[ip][0] == "tpl":
        (cur_state, ip) = tpl(cur_state, commands[ip], ip)
    if commands[ip][0] == "inc":
        (cur_state, ip) = inc(cur_state, commands[ip], ip)
    if commands[ip][0] == "jmp":
        (cur_state, ip) = jmp(cur_state, commands[ip], ip)
        continue
    if commands[ip][0] == "jie":
        (cur_state, ip) = jie(cur_state, commands[ip], ip)
        continue
    if commands[ip][0] == "jio":
        (cur_state, ip) = jio(cur_state, commands[ip], ip)
        continue
    ip = ip + 1

print(cur_state)
