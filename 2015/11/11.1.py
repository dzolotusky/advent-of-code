with open("input11.txt") as f:
    content = [s.strip() for s in f.readlines()]

def increment_str(cur_line_list, index):
    if index == None:
        index = len(cur_line_list) - 1

    if cur_line_list[index] != 'z':
        cur_line_list[index] = chr(ord(cur_line_list[index]) + 1)
    else:
        cur_line_list[index] = 'a'
        increment_str(cur_line_list, index - 1)

for cur_line in content:
    valid = False
    cur_line_list = list(cur_line)
    while not valid:
        increasing_straight = False
        no_increment = False
        pairs = []
        for indx, cur_char in enumerate(cur_line_list):
            if cur_char in "iol":
                cur_line_list[indx] = chr(ord(cur_line_list[indx]) + 1)
                for i in range(indx + 1, len(cur_line_list)):
                    cur_line_list[i] = 'a'
                no_increment = True
                break

            if indx < len(cur_line_list) - 1 and cur_char == cur_line_list[indx + 1]:
                if len(pairs) > 0:
                    if pairs[0] < indx:
                        pairs.append(indx + 1)
                else:
                    pairs.append(indx + 1)

            if indx < len(cur_line_list) - 2 and ord(cur_char) + 1 == ord(cur_line_list[indx + 1]) and ord(cur_char) + 2 == ord(cur_line_list[indx + 2]):
                increasing_straight = True

        if not increasing_straight:
            valid = False
        else:
            if len(pairs) < 2:
                valid = False
            else:
                print("valid: " + str("".join(cur_line_list)))
                valid = True

        if not valid and not no_increment:
            increment_str(cur_line_list, None)