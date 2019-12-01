with open("input22.txt") as f:
    content = f.readlines()

#size_cutoff = 100
size_cutoff = 15

final_line = content[-1]
final_line = final_line.split(' ')[0].split('-')
max_x = 1 + int(final_line[1][1:])
max_y = 1 + int(final_line[2][1:])

nodes = []
for i in range(0, max_y):
    sub_array = [' '] * max_x
    nodes.append(sub_array)


for cur_line in content[2:]:
    cur_line_split = cur_line.strip().split()
    name = cur_line_split[0].split('-')[1:3]
    nodes[int(name[1][1:])][int(name[0][1:])] = cur_line_split[2] + "/" + cur_line_split[1]

def print_grid():
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            print(nodes[i][j], end='')
            if j < len(nodes[i]) - 1:
                print(' -- ', end='')
        print()

print_grid()