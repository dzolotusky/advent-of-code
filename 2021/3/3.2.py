with open("input3.txt") as f:
    content = f.readlines()

o2 = content
co2 = content

for cur_index in range(len(o2[0])):
    count_ones_o2 = [0] * len(content[0].strip())
    count_ones_co2 = [0] * len(content[0].strip())
    most_common_o2 = [0] * len(content[0].strip())
    most_common_co2 = [0] * len(content[0].strip())
    for cur_line in o2:
        for index, cur_char in enumerate(cur_line):
            if cur_char == "1":
                count_ones_o2[index] += 1
    for cur_line in co2:
        for index, cur_char in enumerate(cur_line):
            if cur_char == "1":
                count_ones_co2[index] += 1

    total_lines_o2 = len(o2)
    for index, cur_one_count in enumerate(count_ones_o2):
        if cur_one_count >= (total_lines_o2 / 2):
            most_common_o2[index] = "1"
        else:
            most_common_o2[index] = "0"
    total_lines_co2 = len(co2)
    for index, cur_one_count in enumerate(count_ones_co2):
        if cur_one_count >= (total_lines_co2 / 2):
            most_common_co2[index] = "1"
        else:
            most_common_co2[index] = "0"

    if len(o2) > 1:
        o2 = [l for l in o2 if l[cur_index] == most_common_o2[cur_index]]

    if len(co2) > 1:
        co2 = [l for l in co2 if l[cur_index] != most_common_co2[cur_index]]

o2 = o2[0]
co2 = co2[0]
o2 = "".join(o2)
co2 = "".join(co2)
o2 = int(o2, 2)
co2 = int(co2, 2)

part2 = o2 * co2

print("part 2 = " + str(part2))
