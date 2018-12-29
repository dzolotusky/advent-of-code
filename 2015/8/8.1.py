with open("input8.txt") as f:
    content = f.readlines()

total_chars = 0
total_string_chars = 0

for cur_line in content:
    cur_line = cur_line.strip()
    total_chars = total_chars + len(cur_line)
    # replace // with _ so that the replacement char isn't picked up as the start of another escape sequence
    cur_line = cur_line.replace("\\\\", "_")
    cur_line = cur_line.replace("\\\"", "\"")
    string_chars = len(cur_line) - 2  # drop the two quote
    string_chars = string_chars - cur_line.count("\\x") * 3
    total_string_chars = total_string_chars + string_chars


print("total chars = " + str(total_chars))
print("string chars = " + str(total_string_chars))
print("part 1 = " + str(total_chars - total_string_chars))

# "vvdnb\\x\\uhnxfw\"dpubfkxfmeuhnxisd"