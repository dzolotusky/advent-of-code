with open("input9.txt") as f:
    content = f.readlines()

for cur_line in content:
    full_string = []
    cur_line = cur_line.strip()
    char_index = 0
    while char_index < len(cur_line):
        cur_char = cur_line[char_index]
        if cur_char == '(':
            try:
                next_close = cur_line.index(')', char_index + 1)
                marker = [int(val) for val in cur_line[char_index + 1:next_close].split('x')]
                for count in range(marker[1]):
                    for i in range(marker[0]):
                        full_string.append(cur_line[next_close + 1 + i])
                char_index = next_close + marker[0]
            except ValueError:
                continue
        else:
            full_string.append(cur_char)
        char_index += 1
    # print("".join(full_string))
    print(len(full_string))
