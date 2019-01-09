# find some number where every one of its factors x10 >= puzzle_input
puzzle_input = 29000000
houses = [0] * puzzle_input

for elf in range(1, int(puzzle_input / 11)):
    house_count = 0
    for house_index in range(elf, int(puzzle_input / 11), elf):
        houses[house_index] += elf * 11
        house_count += 1
        if house_count >= 50:
            break

    if elf % 10000 == 0:    # progress indicator
        print(elf)

if len(houses) < 200:   # debug printing
    print(houses)

for house_num, gift_count in enumerate(houses):
    if gift_count >= puzzle_input:
        print("done")
        print(house_num)
        exit()