with open("input25.txt") as f:
    content = f.readlines()

commands = []

for cur_line in content:
    command_split = cur_line.strip().split(' ')
    commands.append(command_split)


def inc(state, command):
    state[ord(command[1]) - ord('a')] += 1
    return state


def out(state, command):
    print(get_value(command[1]), end = ' ')
    return state


def dec(state, command):
    state[ord(command[1]) - ord('a')] -= 1
    return state


def cpy(state, command):
    value = get_value(command[1], state)

    state[ord(command[2]) - ord('a')] = value
    return state


def jnz(state, command, ip):
    value = get_value(command[1], state)

    if value != 0:
        return state, ip + get_value(command[2], state)
    else:
        return state, ip + 1


def tgl(state, command, ip):
    value = get_value(command[1], state)

    other_command_index = ip + value
    if other_command_index > len(commands):
        return state
    other_command = commands[other_command_index]
    if other_command[0] == "inc":
        commands[other_command_index][0] = "dec"
        return state
    if other_command[0] == "jnz":
        commands[other_command_index][0] = "cpy"
        return state
    if len(other_command) == 2:
        commands[other_command_index][0] = "inc"
    if len(other_command) == 3:
        commands[other_command_index][0] = "jnz"
    return state


def get_value(cur_value, state):
    try:
        value = int(cur_value)
    except ValueError:
        value = int(state[ord(cur_value) - ord('a')])
    return value


cur_state = [0, 0, 0, 0]

ip = 0
while ip in range(len(commands)):
    print(str(ip) + ":" + str(commands[ip]) + " " + str(cur_state))
    try:
        if commands[ip][0] == "jnz":
            (cur_state, ip) = jnz(cur_state, commands[ip], ip)
            continue
        if commands[ip][0] == "inc":
            cur_state = inc(cur_state, commands[ip])
        if commands[ip][0] == "out":
            cur_state = out(cur_state, commands[ip])
        if commands[ip][0] == "dec":
            cur_state = dec(cur_state, commands[ip])
        if commands[ip][0] == "cpy":
            cur_state = cpy(cur_state, commands[ip])
        if commands[ip][0] == "tgl":
            cur_state = tgl(cur_state, commands[ip], ip)
    finally:
        ip = ip + 1

print(cur_state)
