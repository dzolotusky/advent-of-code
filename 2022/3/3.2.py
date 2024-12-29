with open("input3.txt") as f:
    content = f.readlines()

total_priority = 0
cur_line_num = 0
while cur_line_num < len(content) - 2:
    duplicate = None
    cur_line = content[cur_line_num]
    next_line = content[cur_line_num + 1]
    third_line = content[cur_line_num + 2]

    for cur_char in cur_line:
        if cur_char in next_line and cur_char in third_line:
            duplicate = cur_char
            break

    if duplicate is not None:
        priority = ord(duplicate)
        if priority >= ord('a'):
            priority -= ord('a')
            priority += 1
        else:
            priority -= ord('A')
            priority += 27
        total_priority += priority

    cur_line_num += 3

part1 = total_priority
print("part 1 = " + str(part1))
