with open("input8.txt") as f:
    content = f.readlines()

part1 = 0

for cur_line in content:
    cur_line_splint = cur_line.split("|")
    digits = cur_line_splint[1].rstrip().strip().split()
    for digit in digits:
        if len(digit) in [2, 4, 3, 7]:
            part1 += 1

print("part 1 = " + str(part1))
