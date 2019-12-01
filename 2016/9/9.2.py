with open("input9.txt") as f:
    content = f.readlines()


def get_char_count(cur_string):
    char_index = 0
    char_count = 0
    while char_index < len(cur_string):
        cur_char = cur_string[char_index]
        if cur_char == '(':
            try:
                next_close = cur_string.index(')', char_index + 1)
                marker = [int(val) for val in cur_string[char_index + 1:next_close].split('x')]
                char_count += marker[1] * get_char_count(cur_string[next_close + 1:next_close + marker[0] + 1])
                char_index = next_close + marker[0] + 1
            except ValueError:
                print("boo")
                continue
        else:
            char_count += 1
            char_index += 1
    return char_count


for cur_line in content:
    char_count = get_char_count(cur_line.strip())
    print(char_count)
