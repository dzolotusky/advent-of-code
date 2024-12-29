with open("input5.txt") as f:
    content = f.readlines()
stacks = {}

for line_num, cur_line in enumerate(content):
    if "[" not in cur_line:
        break

    indx = 0
    while indx < len(cur_line):
        if cur_line[indx - 1] == "[":
            cur_char = cur_line[indx]
            stack_num = (int((indx / 4)) + 1)
            if stack_num not in stacks:
                stacks[stack_num] = []
            stacks[stack_num].insert(0, cur_char)
        indx += 1
line_num += 1
while line_num < len(content):
    cur_line = content[line_num].strip()
    line_num += 1
    if "move" not in cur_line:
        continue
    cur_line_split = cur_line.split()
    num_to_move = int(cur_line_split[1])
    move_from = int(cur_line_split[3])
    move_to = int(cur_line_split[5])

    for num_moved in range(num_to_move):
        stacks[move_to].append(stacks[move_from].pop())

part1 = []
stack_nums = list(stacks.keys())
stack_nums.sort()
for cur_stack_num in stack_nums:
    cur_stack = stacks[cur_stack_num]
    part1.append(cur_stack[-1])
print("part 1 = " + "".join(part1))
