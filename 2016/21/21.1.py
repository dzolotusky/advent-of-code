with open("input21.txt") as f:
    content = f.readlines()

#password = "abcde"
password = "abcdefgh"

ops = []
for cur_line in content:
    args = None
    cur_line_split = cur_line.strip().split()
    if cur_line_split[0] == "swap":
        if cur_line_split[1] == "position":
            name = "sp"
        else:
            name = "sl"
        args = [cur_line_split[2], cur_line_split[-1]]
    if cur_line_split[0] == "reverse":
        name = "rev"
        args = [cur_line_split[2], cur_line_split[-1]]
    if cur_line_split[0] == "rotate":
        if cur_line_split[1] == "based":
            name = "rb"
            args = [cur_line_split[-1]]
        else:
            name = "rot"
            args = [cur_line_split[1], cur_line_split[2]]
    if cur_line_split[0] == "move":
        name = "mv"
        args = [cur_line_split[2], cur_line_split[-1]]

    ops.append((name, args))


def sp(pwd, args):
    tmp = pwd[int(args[0])]
    pwd_list = list(pwd)
    pwd_list[int(args[0])] = pwd_list[int(args[1])]
    pwd_list[int(args[1])] = tmp
    return "".join(pwd_list)


def sl(pwd, args):
    sp_args = [None, None]
    for cur_index, cur_letter in enumerate(pwd):
        if cur_letter == args[0]:
            sp_args[0] = cur_index
        if cur_letter == args[1]:
            sp_args[1] = cur_index
    return sp(pwd, sp_args)


def rot(pwd, args):
    rot_steps = int(args[1])
    if args[0] == "left":
        rot_steps *= -1
    new_pwd = [None] * len(pwd)
    for cur_index, cur_letter in enumerate(pwd):
        new_pwd[(cur_index + rot_steps) % len(pwd)] = cur_letter
    return "".join(new_pwd)


def rb(pwd, args):
    index = pwd.index(args[0])
    rot_steps = 1 + index + (1 if index > 3 else 0)
    return rot(pwd, ["right", rot_steps])


def rev(pwd: str, args):
    pwd_list = list(pwd)
    section = pwd_list[int(args[0]) : int(args[1]) + 1]
    section.reverse()
    for cur_index, cur_letter in enumerate(section):
        pwd_list[cur_index + int(args[0])] = cur_letter
    return "".join(pwd_list)


def mv(pwd, args):
    letter = pwd[int(args[0])]
    pwd_list = list(pwd)
    del pwd_list[int(args[0])]
    pwd_list.insert(int(args[1]), letter)
    return "".join(pwd_list)

for operation in ops:
    #print(password)
    if operation[0] == "sp":
        password = sp(password, operation[1])
    if operation[0] == "sl":
        password = sl(password, operation[1])
    if operation[0] == "rot":
        password = rot(password, operation[1])
    if operation[0] == "rb":
        password = rb(password, operation[1])
    if operation[0] == "rev":
        password = rev(password, operation[1])
    if operation[0] == "mv":
        password = mv(password, operation[1])

print(password)