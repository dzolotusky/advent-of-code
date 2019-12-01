first_code = 20151125


def next_code(current_code):
    return (current_code * 252533) % 33554393
    # return current_code + 1


def get_code_index(i, j):
    ind = (i - 1) * (j - 1) + int((j + 1) * j / 2) + int((i - 1) * i / 2)
    ind -= 1
    return ind


cur_code = first_code
for i in range(get_code_index(2947, 3029)):
    cur_code = next_code(cur_code)

print(cur_code)
