with open("input15.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
spoken = {}
cur_turn = 1
last_spoken = 0

for num in [int(n) for n in content[0].strip().split(",")]:
    spoken[num] = [cur_turn]
    cur_turn += 1
    last_spoken = num

while cur_turn < 30000002:
    if len(spoken[last_spoken]) == 1:
        last_spoken = 0
    else:
        last_spoken = cur_turn - 1 - spoken[last_spoken][-2]

    if last_spoken not in spoken:
        spoken[last_spoken] = [cur_turn]
    else:
        spoken[last_spoken].append(cur_turn)

    if cur_turn == 2020:
        part1 = last_spoken
    if cur_turn == 30000000:
        part2 = last_spoken

    cur_turn += 1

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))