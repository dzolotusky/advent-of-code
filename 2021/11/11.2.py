with open("input11.txt") as f:
    content = f.readlines()

part2 = 0
grid = []


def increase_adjacent(i, j):
    for i_delta in range(-1, 2):
        if -1 < i + i_delta < len(grid):
            for j_delta in range(-1, 2):
                if i_delta == j_delta == 0:
                    continue
                if -1 < j + j_delta < len(grid[i]):
                    grid[i + i_delta][j + j_delta] += 1
                    if grid[i + i_delta][j + j_delta] == 10 and (i + i_delta, j + j_delta) not in step_flashes:
                        step_flashes.append((i + i_delta, j + j_delta))
                        increase_adjacent(i + i_delta, j + j_delta)


for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = int(content[i][j])

# step
for step_num in range(1, 1000):
    step_flashes = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9:
                if (i, j) not in step_flashes:
                    step_flashes.append((i, j))
                    increase_adjacent(i, j)

    for flashed in step_flashes:
        grid[flashed[0]][flashed[1]] = 0

    if len(step_flashes) == 100:
        part2 = step_num
        break

print("part 2 = " + str(part2))
