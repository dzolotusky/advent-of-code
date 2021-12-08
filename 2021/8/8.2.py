with open("input8.txt") as f:
    content = f.readlines()

part2 = 0
digit_mapping = {}

for cur_line in content:
    digit_mapping = {}
    cur_line_splint = cur_line.split("|")
    digits = cur_line_splint[0].rstrip().strip().split()
    for digit in digits:
        if len(digit) == 2:
            digit_mapping[1] = digit
            continue
        if len(digit) == 4:
            digit_mapping[4] = digit
            continue
        if len(digit) == 3:
            digit_mapping[7] = digit
            continue
        if len(digit) == 7:
            digit_mapping[8] = digit
            continue

    for digit in digits:
        digits_one = digit_mapping[1]
        overlap_with_one = [n for n in digit if n in digits_one]
        digits_four = digit_mapping[4]
        overlap_with_four = [n for n in digit if n in digits_four]
        if len(digit) == 5:
            if len(overlap_with_one) == 2:
                digit_mapping[3] = digit
                continue
            else:
                if len(overlap_with_four) == 2:
                    digit_mapping[2] = digit
                    continue
                else:
                    digit_mapping[5] = digit
                    continue
        if len(digit) == 6:
            if len(overlap_with_one) == 1:
                digit_mapping[6] = digit
                continue
            else:
                if len(overlap_with_four) == 4:
                    digit_mapping[9] = digit
                    continue
                else:
                    digit_mapping[0] = digit
                    continue

    cur_number = []
    displayed_digits = cur_line_splint[1].rstrip().strip().split()
    for displayed in displayed_digits:
        for mapping in digit_mapping:
            overlap = [n for n in digit_mapping[mapping] if n in displayed]
            if len(overlap) == len(displayed) and len(overlap) == len(digit_mapping[mapping]):
                cur_number.append(mapping)
                break
    num = cur_number[0] * 1000 + cur_number[1] * 100 + cur_number[2] * 10 + cur_number[3]
    part2 += num



print("part 2 = " + str(part2))
