with open("input14.txt") as f:
    content = f.readlines()

part1 = 0
paths = {}
polymer = content[0].strip()
pairs = {}

for cur_line in content[2:]:
    cur_line_split = cur_line.split("->")
    start = cur_line_split[0].strip()
    end = cur_line_split[1].strip()
    pairs[start] = end

for step_num in range(10):
    new_polymer = []
    for index in range(len(polymer) - 1):
        pair = polymer[index:index + 2]
        new_polymer.append(pair[0])
        if pair in pairs:
            new_polymer.append(pairs[pair])

    new_polymer.append(polymer[-1])
    polymer = "".join(new_polymer)

char_counts = {}

for cur_char in polymer:
    if cur_char not in char_counts:
        char_counts[cur_char] = 0

    char_counts[cur_char] += 1

max_count = cur_char
min_count = cur_char

for cur_count in char_counts:
    if char_counts[cur_count] > char_counts[max_count]:
        max_count = cur_count
    if char_counts[cur_count] < char_counts[min_count]:
        min_count = cur_count

part1 = char_counts[max_count] - char_counts[min_count]
print("part 1 = " + str(part1))
