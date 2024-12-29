with open("input24.txt") as f:
    content = f.readlines()

# below code generates python code from the input

# inp_counter = 0
# for cur_line in content:
#     cur_line_split = cur_line.strip().split()
#     if cur_line_split[0] == "inp":
#         # print("read input to " + str(cur_line_split[1]))
#         print(str(cur_line_split[1]) + " = w" + str(inp_counter))
#         inp_counter += 1
#     if cur_line_split[0] == "add":
#         print(str(cur_line_split[1]) + " = " + str(cur_line_split[1]) + "+" + str(cur_line_split[2]))
#     if cur_line_split[0] == "mul":
#         print(str(cur_line_split[1]) + " = " + str(cur_line_split[1]) + "*" + str(cur_line_split[2]))
#     if cur_line_split[0] == "div":
#         print(str(cur_line_split[1]) + " = int(" + str(cur_line_split[1]) + "/" + str(cur_line_split[2]) + ")")
#     if cur_line_split[0] == "mod":
#         print(str(cur_line_split[1]) + " = " + str(cur_line_split[1]) + "%" + str(cur_line_split[2]))
#     if cur_line_split[0] == "eql":
#         print(str(cur_line_split[1]) + " = 1 if " + str(cur_line_split[1]) + "==" + str(cur_line_split[2]) + " else 0")


# below code is Python that evaluates the model number
def full_run(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, x=0, y=0, z=0):
    w = w0
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 2
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w1
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 13
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w2
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 13
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w3
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 9
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w4
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 15
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w5
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 3
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w6
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -7
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 6
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w7
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 5
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w8
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 16
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w9
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 1)
    x = x + 13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 1
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w10
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -4
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 6
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w11
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -9
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 3
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w12
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 7
    y = y * x
    z = z + y
    print((w, x, y, z))
    w = w13
    x = x * 0
    x = x + z
    x = x % 26
    z = int(z / 26)
    x = x + -9
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = y * 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = y * 0
    y = y + w
    y = y + 9
    y = y * x
    z = z + y
    return w, x, y, z


print(full_run(9, 3, 9, 9, 7, 9, 9, 9, 2, 9, 6, 9, 1, 2)) # 0, part 1 answer
print(full_run(8, 1, 1, 1, 1, 3, 7, 9, 1, 4, 1, 8, 1, 1)) # 0, part 2 answer

# 0 = print(full_run(8, 1, 1, 1, 1, 3, 7, 9, 1, 4, 1, 8, 1, 1)) = part 2 answer
# 0 = print(full_run(9, 3, 9, 9, 7, 9, 9, 9, 2, 9, 6, 9, 1, 2)) = part 1 answer
# part1 = 93997999296912
# part2 = 81111379141811