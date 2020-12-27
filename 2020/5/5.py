with open("input5.txt") as f:
    content = f.readlines()

ones = ['B', 'R']
zeros = ['F', 'L']
part1 = 0
part2 = 0
all_ids = []

for cur_line in content:
    cur_line = cur_line.replace(ones[0], "1")
    cur_line = cur_line.replace(ones[1], "1")
    cur_line = cur_line.replace(zeros[0], "0")
    cur_line = cur_line.replace(zeros[1], "0")
    row = int(cur_line[0:7], 2)
    seat = int(cur_line[7:], 2)
    id = row * 8 + seat
    part1 = max(part1, id)
    all_ids.append(id)

for row_num in range(len(all_ids)):
    if row_num not in all_ids and (row_num - 1) in all_ids and (row_num + 1) in all_ids:
        part2 = row_num
        break

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))