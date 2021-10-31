with open("input23.txt") as f:
    content = f.readlines()

part1 = 0
cups = []
cur_cup_index = 0
for cur_line in content:
    if cur_line == '\n':
        continue
    cups = list(cur_line.strip())
    cups = [int(cup_num) for cup_num in cups]


def play_move():
    global cur_cup_index
    removed_cups = cups[cur_cup_index + 1:cur_cup_index+4]
    if len(removed_cups) < 3:
        removed_cups = removed_cups + cups[0:3 - len(removed_cups)]

    destination_cup = cups[cur_cup_index] - 1

    if destination_cup < min(cups):
        destination_cup = max(cups)

    while destination_cup in removed_cups:
        destination_cup -= 1

        if destination_cup < min(cups):
            destination_cup = max(cups)

    destination_cup_indx = cups.index(destination_cup)

    my_cup = cups[(cur_cup_index + 1) % len(cups)]
    counter = 1
    while my_cup != destination_cup:
        cups[(cur_cup_index + counter) % len(cups)] = cups[(cur_cup_index + 3 + counter) % len(cups)]
        counter += 1
        my_cup = cups[(cur_cup_index + counter) % len(cups)]
    cups[destination_cup_indx] *= -1

    destination_cup_indx = cups.index(destination_cup)
    for counter in range(0,3):
        cups[(destination_cup_indx + 1 + counter) % len(cups)] = removed_cups[counter]
    cur_cup_index = (cur_cup_index + 1) % len(cups)


def print_cups(cups_to_print, current_cup_indx):
    for index, cup_num in enumerate(cups_to_print):
        if index == current_cup_indx:
            print("(", end='')

        print(cup_num, end='')

        if index == current_cup_indx:
            print(") ", end='')
        else:
            if index != current_cup_indx - 1:
                print("  ", end='')
            else:
                print(" ", end='')
    print()


for move_num in range(0,100):
    play_move()

#print_cups(cups, cur_cup_index)

one_index = cups.index(1)
part1 = cups[one_index + 1:] + cups[:one_index]
part1 = [str(cup) for cup in part1]
print("part 1 = " + "".join(part1))