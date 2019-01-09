# find some number where every one of its factors x10 >= puzzle_input
puzzle_input = 150  # random test value
houses = [0] * puzzle_input

for elf in range(1, int(puzzle_input / 10)):
    for house_index in range(elf, int(puzzle_input / 10), elf):
        houses[house_index] += elf * 10

    if elf % 10000 == 0:    # progress indicator
        print(elf)

if len(houses) < 200:   # debug printing
    print(houses)

for house_num, gift_count in enumerate(houses):
    if gift_count >= puzzle_input:
        print("done")
        print(house_num)
        exit()