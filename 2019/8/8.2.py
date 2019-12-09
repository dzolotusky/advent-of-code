with open("input8.txt") as f:
    content = f.readlines()

#width = 2
#height = 2

width = 25
height = 6

image = list(map(int, content[0].strip()))

image_grid = []
for i in range(height):
    sub_array = [2] * width
    image_grid.append(sub_array)


def print_grid():
    for i in range(len(image_grid)):
        for j in range(len(image_grid[i])):
            print('.' if image_grid[i][j] == 0 else '*', end='')
            if j < len(image_grid[i]) - 1:
                print('', end='')
        print()


#print_grid()

num_layers = int(len(image) / (width * height))
layer_length = width * height
num_zeros = []
num_ones = []
num_twos = []

for cur_layer in range(num_layers):
    for cur_w in range(width):
        for cur_h in range(height):
            if image_grid[cur_h][cur_w] == 2:
                image_grid[cur_h][cur_w] = image[layer_length * cur_layer + cur_w + (cur_h * width)]

print_grid()
