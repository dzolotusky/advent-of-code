with open("input6.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
yes_in_group = {}
num_in_group = 0

for cur_line in content:
    if cur_line == "\n":
        part1 += len(yes_in_group)
        for yes in yes_in_group:
            if yes_in_group[yes] == num_in_group:
                part2 += 1
        yes_in_group = {}
        num_in_group = 0
        continue

    num_in_group += 1
    for answer in cur_line:
        if answer == "\n":
            continue
        if answer not in yes_in_group:
            yes_in_group[answer] = 1
        else:
            yes_in_group[answer] += 1

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))