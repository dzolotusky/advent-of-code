import sys

with open("input7.txt") as f:
    content = f.readlines()

all_positions = [int(num) for num in content[0].strip().split(",")]

min_pos = min(all_positions)
max_pos = max(all_positions)
min_steps = sys.maxsize
best_pos = -1

for cur_pos in range(min_pos, 1 + max_pos):
    steps = [abs(pos - cur_pos) for pos in all_positions]
    total_steps = sum(steps)
    if total_steps < min_steps:
        min_steps = total_steps
        best_pos = cur_pos


part1 = min_steps

print("part 1 = " + str(part1))
