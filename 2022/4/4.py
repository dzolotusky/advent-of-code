with open("input4.txt") as f:
    content = f.readlines()

part1 = part2 = 0
for cur_line in content:
    pairs = cur_line.split(",")
    pair1 = [int(coord) for coord in pairs[0].split("-")]
    pair2 = [int(coord) for coord in pairs[1].split("-")]
    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1] or \
            pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        part1 += 1

    if pair1[0] <= pair2[1] and pair1[1] >= pair2[0] or \
            pair1[0] >= pair2[1] and pair1[1] <= pair2[0]:
        part2 += 1

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))
