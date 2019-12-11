with open("input10.txt") as f:
    content = f.readlines()

grid = []
for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = content[i][j]


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


print("Initial state:")
print_grid()

asteroids = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            asteroids.append((i, j))

max_visible = 0
best_asteroid = None

for cur_asteroid in asteroids:
    others = asteroids.copy()
    others.remove(cur_asteroid)
    others_deltas = []
    for cur_other in others:
        cur_other_delta = (cur_other[0] - cur_asteroid[0], cur_other[1] - cur_asteroid[1])
        cur_other_delta_ratio = cur_other_delta[0] / cur_other_delta[1] if cur_other_delta[1] != 0 else 100 if \
        cur_other_delta[0] > 0 else -100

        if cur_other_delta_ratio == 0 and cur_other_delta[1] != 0:
            cur_other_delta_ratio = 150 if cur_other_delta[1] > 0 else -150

        if cur_other_delta[0] < 0 and cur_other_delta[1] < 0:
            cur_other_delta_ratio = cur_other_delta_ratio * -1

        if cur_other_delta[0] < 0 and cur_other_delta[1] > 0:
            cur_other_delta_ratio = cur_other_delta_ratio * 1j

        if cur_other_delta[0] > 0 and cur_other_delta[1] < 0:
            cur_other_delta_ratio = cur_other_delta_ratio * -1j

        cur_other_delta = (cur_other_delta_ratio)
        others_deltas.append(cur_other_delta)

    #    print (str(cur_asteroid) + " : " + str(others_deltas))
    num_visible = len(set(others_deltas))
    print(str(cur_asteroid) + " : " + str(num_visible))
    if num_visible > max_visible:
        max_visible = num_visible
        best_asteroid = cur_asteroid

best_asteroid = (best_asteroid[1], best_asteroid[0])
print("best = " + str(best_asteroid))
print("part 1 = " + str(max_visible))
