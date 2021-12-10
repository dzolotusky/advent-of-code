with open("input10.txt") as f:
    content = f.readlines()

part2 = 0
open_stack = []
openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
closer_to_opener_map = {")":"(", "]":"[", "}":"{", ">":"<"}
scores = {"(": 1, "[": 2, "{": 3, "<": 4}
total_scores = []

for cur_line in content:
    cur_line = cur_line.strip()
    open_stack = []
    for cur_char in cur_line:
        if cur_char in openers:
            open_stack.append(cur_char)
        if cur_char in closers:
            if open_stack.pop() != closer_to_opener_map[cur_char]:
                open_stack = []
                break   # these are corrupt
    if len(open_stack) > 0:
        total_score = 0
        open_stack.reverse()
        for remaining_char in open_stack:
            total_score *= 5
            total_score += scores[remaining_char]
        total_scores.append(total_score)

total_scores.sort()
part2 = total_scores[int(len(total_scores) / 2)]
print("part 2 = " + str(part2))
