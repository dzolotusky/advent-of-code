from curses.ascii import isdigit

with open("input7.txt") as f:
    content = f.readlines()

cur_stack = []
directories = {"/": 0}

part1 = 0
for cur_line in content:
    cur_line_split = cur_line.split()
    if cur_line[0] == "$" and "cd" == cur_line_split[1]:
        new_dir = cur_line_split[-1]
        if new_dir == "/":
            cur_stack = []

        if new_dir == "..":
            cur_stack.pop()
        else:
            path = "/".join(cur_stack) + "/" + new_dir
            path = path[1:]
            if path not in directories:
                directories[path] = 0
            cur_stack.append(new_dir)

    if isdigit(cur_line[0]):
        file_size = int(cur_line.split()[0])
        cur_path = ""
        for cur_dir in cur_stack:
            if cur_dir == "/":
                cur_dir = ""
            if cur_path == "/":
                cur_path = ""
            cur_path = cur_path + "/" + cur_dir
            directories[cur_path] += file_size

for cur_dir in directories:
    if directories[cur_dir] <= 100000:
        part1 += directories[cur_dir]

print("part1 = " + str(part1))