with open("input8.txt") as f:
    content = f.readlines()

#width = 3
#height = 2

width = 25
height = 6

image = list(map(int, content[0].strip()))
num_layers = int(len(image) / (width * height))
layer_length = width * height
num_zeros = []
num_ones = []
num_twos = []

for cur_layer in range(num_layers):
    num_zero = 0
    num_one = 0
    num_two = 0
    for cur_w in range(width):
        for cur_h in range(height):
            if image[layer_length * cur_layer + cur_w + (cur_h * width)] == 0:
                num_zero += 1
            if image[layer_length * cur_layer + cur_w + (cur_h * width)] == 1:
                num_one += 1
            if image[layer_length * cur_layer + cur_w + (cur_h * width)] == 2:
                num_two += 1
    num_zeros.append(num_zero)
    num_ones.append(num_one)
    num_twos.append(num_two)

min_zero_layer = num_zeros.index(min(num_zeros))

part1 = num_ones[min_zero_layer] * num_twos[min_zero_layer]
print("part1 = " + str(part1))