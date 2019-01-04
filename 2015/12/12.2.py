with open("input12.txt") as f:
    content = f.readlines()

cur_line = content[0]

stack_of_curly = []
remove = []
for indx, cur_char in enumerate(cur_line):
    if cur_char == '{':
        stack_of_curly.append((indx, False))
    if cur_char == ':' and cur_line[indx + 1] == '"' and cur_line[indx + 2] == 'r' and cur_line[indx + 3] == 'e' and cur_line[indx + 4] == 'd':
        if len(stack_of_curly) > 0:
            (start, redness) = stack_of_curly.pop()
            stack_of_curly.append((start, True))
    if cur_char == '}':
        value = stack_of_curly.pop()
        if value[1]:
            remove.append((value[0], indx))

for item in remove:
    cur_line = cur_line[:item[0]] + ' ' * (item[1] - item[0]) + cur_line[item[1]:]

cur_line = cur_line.replace("[", " ").replace("]", " ")
cur_line = cur_line.replace(":", " ")
cur_line = cur_line.replace(",", " ")
cur_line = cur_line.replace("{", " ").replace("}", " ")

cur_line_split = cur_line.split(" ")

total_value = 0
for value in cur_line_split:
    try:
        value = int(value)
        total_value = total_value + value
    except ValueError:
        continue

print(total_value)