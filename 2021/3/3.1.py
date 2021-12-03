with open("input3.txt") as f:
    content = f.readlines()

count_ones = [0] * len(content[0].strip())

for cur_line in content:
    for index, cur_char in enumerate(cur_line):
        if cur_char == "1":
            count_ones[index] += 1

epsilon = [None] * len(content[0].strip())
gamma = [None] * len(content[0].strip())

total_lines = len(content)
for index, cur_one_count in enumerate(count_ones):
    if cur_one_count > (total_lines / 2):
        epsilon[index] = "1"
        gamma[index] = "0"
    else:
        epsilon[index] = "0"
        gamma[index] = "1"

gamma = "".join(gamma)
epsilon = "".join(epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

part1 = gamma * epsilon

print("part 1 = " + str(part1))