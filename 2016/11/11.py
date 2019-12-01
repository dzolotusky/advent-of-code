with open("input11.txt") as f:
    content = f.readlines()

floors = []
elevator = 0
all_items = []

for cur_line in content:
    cur_line_split = cur_line.strip().split(' ')
    cur_floor = []
    floors.append(cur_floor)
    if cur_line_split[4] == "nothing":
        continue

    floor_contents = cur_line_split[4:]
    while 'a' in floor_contents:
        floor_contents.remove('a')

    while 'and' in floor_contents:
        floor_contents.remove('and')

    word_index = 0
    while word_index < len(floor_contents):
        item = (floor_contents[word_index][0] + floor_contents[word_index + 1][0]).upper()
        cur_floor.append(item)
        all_items.append(item)
        word_index += 2

all_items.sort()


def print_floors():
    for index in range(len(floors)):
        cur_floor_num = len(floors) - index
        print("F" + str(cur_floor_num), end=' ')
        if elevator == cur_floor_num - 1:
            print('E', end=' ')
        else:
            print('.', end=' ')

        print()


print(floors)
print_floors()
