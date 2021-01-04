with open("input10.txt") as f:
    content = [int(s) for s in f.readlines()]

part1 = 0
part2 = 0

content.append(0)
content.sort()
content.append(content[-1] + 3)

diff_one = 0
diff_three = 0
for cur_index in range(len(content) - 1):
    if content[cur_index + 1] - content[cur_index] == 1:
        diff_one += 1

    if content[cur_index + 1] - content[cur_index] == 3:
        diff_three += 1

part1 = diff_one * diff_three

combs = {0: 1}

for adapter in content[1:]:
    my_combs = 0
    for look_back in range(1, 4):
        if (adapter - look_back) in combs:
            my_combs += combs[(adapter - look_back)]
    combs[adapter] = my_combs

part2 = combs[content[-1]]
print("part 1 = " + str(part1))
print("part 2 = " + str(part2))