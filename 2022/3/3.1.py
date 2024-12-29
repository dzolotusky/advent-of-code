with open("input3.txt") as f:
    content = f.readlines()

total_priority = 0
for cur_line in content:
    duplicate = None
    compartment_size = int(len(cur_line) / 2)
    first_compartment = cur_line[:compartment_size]
    second_compartment = cur_line[compartment_size:]
    for cur_char in first_compartment:
        if cur_char in second_compartment:
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

part1 = total_priority
print("part 1 = " + str(part1))
