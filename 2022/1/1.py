with open("input1.txt") as f:
    content = f.readlines()
content.append("\n")

max_elf = cur_elf = 0
all_elves = []

for cur_line in content:
    if cur_line == "\n":
        all_elves.append(cur_elf)
        if cur_elf > max_elf:
            max_elf = cur_elf

        cur_elf = 0
    else:
        cur_elf += int(cur_line)

part1 = max_elf

all_elves.sort()
part2 = sum(all_elves[-3:])

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))