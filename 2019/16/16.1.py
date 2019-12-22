with open("test_input16.txt") as f:
    content = f.readlines()

input_signal = list(map(int, content[0].strip()))
base_pattern = [0, 1, 0, -1]

#base_pattern = []
#base_pattern.append([0, 1, 0, -1])
#base_pattern.append([0, 0, 1, 1, 0, 0, -1, -1])
#base_pattern.append([0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1])
#base_pattern.append([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1])
#base_pattern.append([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1])
#base_pattern.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1])
#base_pattern.append([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1])
#base_pattern.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1])

new_base_patterns = []

for input_index, input_element in enumerate(input_signal):
    input_index += 1
    new_base_pattern = []
    output_index = 0
    input_element_index = -1
    while output_index < (len(input_signal) + 1):
        input_element_index += 1
        for loop_index in range(min(input_index, (len(input_signal) - output_index + 1))):
            if output_index != 0:
                new_base_pattern.append(base_pattern[(input_element_index) % len(base_pattern)])
            output_index += 1

    new_base_patterns.append(new_base_pattern)

# print(new_base_patterns)
# for pat in new_base_patterns:
#     print(len(pat))
#
# print("total")
# print (len(new_base_patterns))

for stage in range(100):
    output_signal = []
    for cur_base in new_base_patterns:
        total = 0
        for el_index, input_el in enumerate(input_signal):
            total += input_el * cur_base[el_index]
        output_signal.append(abs(total) % 10)
    input_signal = output_signal

print(output_signal)
print("".join(map(str, output_signal)))
