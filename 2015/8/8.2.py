with open("input8.txt") as f:
    content = f.readlines()

total_chars = 0
total_encoded_chars = 0

for cur_line in content:
    cur_line = cur_line.strip()
    total_chars = total_chars + len(cur_line)
    encoded_chars = len(cur_line) + 2
    encoded_chars = encoded_chars + cur_line.count("\\") + cur_line.count("\"")
    total_encoded_chars = total_encoded_chars + encoded_chars

print("total chars = " + str(total_chars))
print("encoded chars = " + str(total_encoded_chars))
print("part 2 = " + str(total_encoded_chars - total_chars))
