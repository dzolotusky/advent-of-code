with open("test_input6.txt") as f:
    content = f.readlines()

part1 = -1
last3 = []
for cur_line in content:
    for index, cur_char in enumerate(cur_line):
        if len(last3) == 3:
            if cur_char not in last3 and len(set(last3)) == len(last3):
                part1 = index + 1
                break

        last3.append(cur_char)
        if len(last3) > 3:
            last3.remove(last3[0])

print("part1 = " + str(part1))