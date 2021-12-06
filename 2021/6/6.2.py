with open("input6.txt") as f:
    content = f.readlines()

covered = {}
all_fish = [0] * 9

for cur_num in [int(n) for n in content[0].split(",")]:
    all_fish[cur_num] += 1

new_fish = 0
for day in range(256):
    new_fish = all_fish[0]
    for i in range(len(all_fish) - 1):
        all_fish[i] = all_fish[i + 1]
    all_fish[8] = new_fish
    all_fish[6] += new_fish


part2 = sum(all_fish)

print("part 2 = " + str(part2))
