with open("input12.txt") as f:
    content = f.readlines()

commands = []

for cur_line in content:
    command_split = cur_line.strip().split(' ')
    commands.append(command_split)


def inc(state, command):
    state[ord(command[1]) - ord('a')] += 1
    return state


def dec(state, command):
    state[ord(command[1]) - ord('a')] -= 1
    return state


def cpy(state, command):
    try:
        value = int(command[1])
    except ValueError:
        value = int(state[ord(command[1]) - ord('a')])

    state[ord(command[2]) - ord('a')] = value
    return state


def jnz(state, command, ip):
    try:
        value = int(command[1])
    except ValueError:
        value = int(state[ord(command[1]) - ord('a')])

    if value != 0:
        return state, ip + int(command[2])
    else:
        return state, ip + 1


# print(commands)

cur_state = [0, 0, 1, 0]

ip = 0
while ip in range(len(commands)):
    # print(str(ip) + ":" + str(commands[ip]) + " " + str(cur_state))
    if commands[ip][0] == "jnz":
        (cur_state, ip) = jnz(cur_state, commands[ip], ip)
        continue
    if commands[ip][0] == "inc":
        cur_state = inc(cur_state, commands[ip])
    if commands[ip][0] == "dec":
        cur_state = dec(cur_state, commands[ip])
    if commands[ip][0] == "cpy":
        cur_state = cpy(cur_state, commands[ip])
    ip = ip + 1

print(cur_state)
