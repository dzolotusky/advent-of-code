with open("input16.txt") as f:
    content = f.readlines()

input_content = 10000 * content[0].strip()
input_signal = list(map(int, input_content))
message_offset = int(input_content[:7])

output_signal = input_signal[message_offset:]

for stage in range(100):
    #print(stage)
    last_elem = len(output_signal) - 1
    for output_index in range(1, last_elem + 1):
        output_signal[last_elem - output_index] += output_signal[1 + last_elem - output_index]
        output_signal[last_elem - output_index] %= 10
#    output_string = "".join(map(str, output_signal))
#    print(output_string)

print("Part 2 = " + "".join(map(str, output_signal[0:8])))