import sys

with open("input7.txt") as f:
    content = f.readlines()

all_positions = [int(num) for num in content[0].strip().split(",")]

min_pos = min(all_positions)
max_pos = max(all_positions)
min_steps = sys.maxsize
best_pos = -1

f2s = {}


def steps_to_fuel(steps):
    if steps in f2s:
        return f2s[steps]
    else:
        fuel = 0
        for i in range(steps + 1):
            fuel += i
            f2s[steps] = fuel
        return fuel


for cur_pos in range(min_pos, 1 + max_pos):
    steps = [steps_to_fuel(abs(pos - cur_pos)) for pos in all_positions]
    total_steps = sum(steps)
    if total_steps < min_steps:
        min_steps = total_steps
        best_pos = cur_pos

part2 = min_steps

print("part 2 = " + str(part2))
