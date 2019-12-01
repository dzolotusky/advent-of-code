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
    real_name = []
    for cur_char in room[0]:
        if cur_char == '-':
            new_char = ' '
        else:
            char_num = ord(cur_char) - ord('a')
            char_num += room[1]
            char_num %= 26
            new_char = chr(ord('a') + char_num)

        real_name.append(new_char)

    unencrypted_name = "".join(real_name)
    if "north" in unencrypted_name:
        print(unencrypted_name)
        print(room[1])
