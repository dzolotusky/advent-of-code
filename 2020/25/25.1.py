with open("input25.txt") as f:
    content = f.readlines()

part1 = 0
card_public_key = int(content[0])
door_public_key = int(content[1])
subject_num = 7

door_val = 1
card_val = 1

door_loop_size = -1
card_loop_size = -1
loop_num = 1
while door_loop_size == -1 or card_loop_size == -1:
    if door_loop_size == -1:
        door_val *= subject_num
        door_val %= 20201227

        if door_val == door_public_key:
            door_loop_size = loop_num

    if card_loop_size == -1:
        card_val *= subject_num
        card_val %= 20201227

        if card_val == card_public_key:
            card_loop_size = loop_num
    loop_num += 1

max_loop_size = max(door_loop_size, card_loop_size)
door_val = 1
card_val = 1
for loop_num in range(max_loop_size):
    if loop_num < card_loop_size:
        door_val *= door_public_key
        door_val %= 20201227

        if loop_num == card_loop_size - 1:
            door_encryption_key = door_val

    if loop_num < door_loop_size:
        card_val *= card_public_key
        card_val %= 20201227

        if loop_num == door_loop_size - 1:
            card_encryption_key = card_val

if card_encryption_key != door_encryption_key:
    print("keys don't match")
else:
    print("part 1 = " + str(card_encryption_key))