with open("input6.txt") as f:
    content = f.readlines()

covered = {}
all_fish = [int(f) for f in content[0].split(",")]

for day in range(80):
    new_fish = []
    for index, cur_fish in enumerate(all_fish):
        if cur_fish == 0:
            all_fish[index] = 6
            new_fish.append(8)
        else:
            all_fish[index] -= 1
    all_fish = all_fish + new_fish

part1 = len(all_fish)

print("part 1 = " + str(part1))
