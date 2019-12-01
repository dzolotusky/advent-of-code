from blist import blist

input = 3001330

elves = blist([])

for i in range(input):
    elves.append((i + 1, 1))


def play_round():
    global elves
    ind = 0
    while ind < len(elves):
        num_elves = len(elves)
        next_elf = (ind + int(num_elves / 2)) % num_elves
        elves[ind] = (elves[ind][0], elves[ind][1] + elves[next_elf][1])
        del elves[next_elf]
        if next_elf > ind:
            ind += 1


remaining = [1, 2]
while (len(remaining) > 1):
    play_round()
    remaining = [e for e, c in elves]
    print(str(len(remaining)) + ":" + str(remaining))

print("Part 2 = " + str(remaining[0]))