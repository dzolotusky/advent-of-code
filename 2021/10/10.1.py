with open("input10.txt") as f:
    content = f.readlines()

part1 = 0
open_stack = []
openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
closer_to_opener_map = {")":"(", "]":"[", "}":"{", ">":"<"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

for cur_line in content:
    cur_line = cur_line.strip()
    open_stack = []
    for cur_char in cur_line:
        if cur_char in openers:
            open_stack.append(cur_char)
        if cur_char in closers:
            if open_stack.pop() != closer_to_opener_map[cur_char]:
                part1 += scores[cur_char]
                break

print("part 1 = " + str(part1))
