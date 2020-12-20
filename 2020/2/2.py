with open("input2.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0

for cur_line in content:
    command_str = cur_line.split(':')
    rule = command_str[0]
    range = rule.split(" ")[0]
    min = int(range.split("-")[0])
    max = int(range.split("-")[1])
    letter = rule.split(" ")[1].strip()
    password = command_str[1]
    num_occurences = password.count(letter)
    if num_occurences >= min and num_occurences <= max:
        part1 += 1

    if (password[min] == letter and password[max] != letter) or (password[min] != letter and password[max] == letter):
        part2 += 1

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))