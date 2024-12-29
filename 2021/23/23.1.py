with open("input22.txt") as f:
    content = f.readlines()

part1 = 0
hallway = ['.'] * 11
rooms_doors= [3,5,7,9]

for cur_line in content[2:3]:
    for char_index, cur_char in enumerate(cur_line):
        if cur_char != '#':


print("part 1 = " + str(part1))