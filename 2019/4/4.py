num_passwords_part_1 = 0
num_passwords_part_2 = 0

for num in range(183564, 657474):
    pw = str(num)
    double_p1 = False
    double_p2 = False
    decrease = False
    for i in range(0, 5):
        if pw[i] == pw[i + 1]:
            double_p1 = True

            if i > 0 and pw[i] == pw[i - 1]:
                continue
            if i < 4 and pw[i] == pw[i + 2]:
                continue
            double_p2 = True

        if pw[i] > pw[i + 1]:
            decrease = True

    if double_p1 and not decrease:
        num_passwords_part_1 += 1

    if double_p2 and not decrease:
        num_passwords_part_2 += 1

print("part 1 = " + str(num_passwords_part_1))
print("part 2 = " + str(num_passwords_part_2))
