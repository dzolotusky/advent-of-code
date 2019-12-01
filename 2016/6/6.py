with open("input6.txt") as f:
    content = f.readlines()

occurences = []
for ind in range(len(content[0])):
    occurences.append({})

for cur_line in content:
    for char_index, cur_char in enumerate(cur_line):
        if cur_char in occurences[char_index]:
            occurences[char_index][cur_char] += 1
        else:
            occurences[char_index][cur_char] = 0

part1 = []
part2 = []
for column in occurences:
    col_as_list = list(column.items())
    col_as_list.sort(key=lambda l: (l[1] * -1))
    part1.append(col_as_list[0][0])
    part2.append(col_as_list[-1][0])

print("part 1 = " + "".join(part1).strip())
print("part 2 = " + "".join(part2).strip())
