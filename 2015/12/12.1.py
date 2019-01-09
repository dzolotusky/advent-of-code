with open("input12.txt") as f:
    content = f.readlines()

cur_line = content[0]
cur_line = cur_line.replace("[", " ").replace("]", " ")
cur_line = cur_line.replace("{", " ").replace("}", " ")
cur_line = cur_line.replace(":", " ")
cur_line = cur_line.replace(",", " ")
cur_line_split = cur_line.split(" ")

total_value = 0
for value in cur_line_split:
    try:
        value = int(value)
        total_value = total_value + value
    except ValueError:
        continue

print(total_value)
