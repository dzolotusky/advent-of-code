with open("input1.txt") as f:
    content = f.readlines()

numbers = [int(i) for i in content]

part1 = 0
part2 = 0

for num1 in numbers:
    for num2 in numbers:
        if num1 + num2 == 2020:
            part1 = num1 * num2

        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                part2 = num1 * num2 * num3

print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
