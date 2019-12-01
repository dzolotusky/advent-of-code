with open("input20.txt") as f:
    content = f.readlines()

ranges = []
for cur_line in content:
    ranges.append([int(val) for val in cur_line.split('-')])

test_ip = 0
while True:
    in_range = False
    for range in ranges:
        if range[0] <= test_ip <= range[1]:
            in_range = True
            test_ip = range[1] + 1
            continue
    if not in_range:
        break

print("part 1 = " + str(test_ip))
