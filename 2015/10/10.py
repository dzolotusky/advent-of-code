# input = "1"
input = "1113122113"

for i in range(50):
    output = []
    last_char = None
    count = 0
    for cur_char in input:
        if cur_char == last_char:
            count = count + 1
        else:
            if last_char is not None:
                output.append(str(count))
                output.append(last_char)
            count = 1
            last_char = cur_char

    output.append(str(count))
    output.append(last_char)

    input = "".join(output)
    print(str(i + 1) + ":" + str(len(input)))  # + ":"+ input)
