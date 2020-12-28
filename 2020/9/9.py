with open("input9.txt") as f:
    content = [int(s) for s in f.readlines()]

part1 = 0
part2 = 0
preamble_len = 25

for line_num in range(preamble_len, len(content)):
    cur_val = content[line_num]
    preamble = content[line_num - preamble_len : line_num]
    valid = False
    for pre_val in preamble:
        if (cur_val - pre_val) in preamble:
            valid = True
            break
    if not valid:
        part1 = cur_val
        break

for cur_start_num in range(0, len(content)):
    total = content[cur_start_num]
    smallest = content[cur_start_num]
    largest = content[cur_start_num]
    for num_to_add in range(cur_start_num + 1, len(content)):
        total += content[num_to_add]
        smallest = min(smallest, content[num_to_add])
        largest = max(largest, content[num_to_add])
        if total == part1:
            part2 = smallest + largest
            break
        if total > part1:
            break

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))