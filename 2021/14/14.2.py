with open("input14.txt") as f:
    content = f.readlines()

part2 = 0
paths = {}
polymer = content[0].strip()
pair_rules = {}
pairs = {}

for index in range(len(polymer) - 1):
    cur_pair = polymer[index:index + 2]
    if cur_pair not in pairs:
        pairs[cur_pair] = 0
    pairs[cur_pair] += 1

for cur_line in content[2:]:
    cur_line_split = cur_line.split("->")
    start = cur_line_split[0].strip()
    end = cur_line_split[1].strip()
    pair_rules[start] = end

for step_num in range(40):
    new_pairs = {}
    for rule in pair_rules:
        if rule in pairs:
            pair_count = pairs[rule]
            new_char = pair_rules[rule]
            new_pair_one = rule[0] + new_char
            new_pair_two = new_char + rule[1]
            if new_pair_one not in new_pairs:
                new_pairs[new_pair_one] = 0
            if new_pair_two not in new_pairs:
                new_pairs[new_pair_two] = 0
            new_pairs[new_pair_one] += pair_count
            new_pairs[new_pair_two] += pair_count

    pairs = new_pairs


char_counts = {}
for cur_pair in pairs:
    pair_count = pairs[cur_pair]
    for cur_char in cur_pair:
        if cur_char not in char_counts:
            char_counts[cur_char] = 0

        char_counts[cur_char] += pair_count

max_count = cur_char
min_count = cur_char


for cur_count in char_counts:
    char_counts[cur_count] = int(char_counts[cur_count] / 2)

char_counts[polymer[0]] += 1
char_counts[polymer[-1]] += 1

for cur_count in char_counts:
    if char_counts[cur_count] > char_counts[max_count]:
        max_count = cur_count
    if char_counts[cur_count] < char_counts[min_count]:
        min_count = cur_count

part2 = char_counts[max_count] - char_counts[min_count]
print("part 2 = " + str(part2))