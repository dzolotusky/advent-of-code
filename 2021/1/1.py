import sys
with open("input1.txt") as f:
    content = f.readlines()

numbers = [int(i) for i in content]

part1 = 0
part2 = 0

prev_num = sys.maxsize
window_sum = 0

for index, num in enumerate(numbers):
    if num > prev_num:
        part1 += 1
    prev_num = num

    prev_window_sum = window_sum

    if index > 2:
        window_sum -= numbers[index - 3]
    window_sum += num
    if index > 2:
        if window_sum > prev_window_sum:
            part2 += 1


print("part 1 = " + str(part1))

print("part 2 = " + str(part2))
