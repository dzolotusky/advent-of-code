first_code = 1#20151125
codes = []


def next_code(current_code):
    #return (current_code * 252533) % 33554393
    return current_code + 1


cur_code = first_code
codes.append(cur_code)
for i in range(1000):
    cur_code = next_code(cur_code)
    codes.append(cur_code)

def get_code(i,j):
    ind = (i-1) * (j-1) + int((j+1) * j / 2) + int((i-1) * i / 2)
    ind -= 1
    return codes[ind]

grid = []
for i in range(0,10):
    sub_array = ['.']*10
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range (len(grid[i])):
        grid[i][j] = get_code(i,j)


def print_grid():
    for i in range(1, len(grid)):
        for j in range (1, len(grid[i])):
            print(grid[i][j], end=' ')
        print()

print(get_code(4,2))
print(get_code(1,5))
#print_grid()
