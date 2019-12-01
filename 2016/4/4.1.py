with open("input4.txt") as f:
    content = f.readlines()

sum_sectors = 0
rooms = []
for cur_line in content:
    sector_start = cur_line.rfind('-')
    checksum_start = cur_line.index('[')

    room_name = cur_line[: sector_start]
    sector_id = int(cur_line[sector_start + 1: checksum_start])
    checksum = cur_line[checksum_start + 1: -2]

    rooms.append((room_name, sector_id, checksum))

for room in rooms:
    letter_dict = {}
    for letter in room[0]:
        if letter == '-':
            continue

        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 0

    letter_list = list(letter_dict.items())
    letter_list.sort(key=lambda l: (l[1] * -1, l[0]))
    checksum = "".join([val for (val, count) in letter_list[0:5]])

    if checksum == room[2]:
        sum_sectors += room[1]

print(sum_sectors)
