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
others_for_best = None

for cur_asteroid in asteroids:
    others = asteroids.copy()
    others.remove(cur_asteroid)
    others_deltas = {}
    for cur_other in others:
        cur_other_delta = (cur_other[0] - cur_asteroid[0], cur_other[1] - cur_asteroid[1])

        cur_other_delta_ratio = cur_other_delta[0] / cur_other_delta[1] if cur_other_delta[1] != 0 else 0 if \
            cur_other_delta[0] < 0 else 200

        if cur_other_delta_ratio == 0 and cur_other_delta[1] != 0:
            cur_other_delta_ratio = 100 if cur_other_delta[1] > 0 else 300

#        if cur_other_delta[0] > 0 and cur_other_delta[1] > 0:
#            cur_other_delta_ratio +=

        if cur_other_delta[0] < 0 and cur_other_delta[1] < 0:
            cur_other_delta_ratio += 350

        if cur_other_delta[0] < 0 < cur_other_delta[1]:
            cur_other_delta_ratio += 50

        if cur_other_delta[0] > 0 > cur_other_delta[1]:
            cur_other_delta_ratio += 250

        if cur_other_delta[0] > 0 and cur_other_delta[1] > 0:
            cur_other_delta_ratio += 150

        if cur_other_delta_ratio in others_deltas:
            others_deltas[cur_other_delta_ratio].append(cur_other)
        else:
            others_deltas[cur_other_delta_ratio] = [cur_other]

    #    print (str(cur_asteroid) + " : " + str(others_deltas))
    num_visible = len(set(others_deltas.keys()))
    #print(str(cur_asteroid) + " : " + str(num_visible))
    if num_visible > max_visible:
        max_visible = num_visible
        best_asteroid = cur_asteroid
        others_for_best = others_deltas

best_asteroid = (best_asteroid[1], best_asteroid[0])
print("best = " + str(best_asteroid))
print("part 1 = " + str(max_visible))

grid[best_asteroid[1]][best_asteroid[0]] = 'X'

print("With Laser Location at " + str(best_asteroid))
print_grid()

#print (others_for_best)
sorted_keys = list(others_for_best.keys())
sorted_keys.sort()
counter = 1
part2 = None
for key in sorted_keys:
    #print(str(counter) + ": " + str(key) + ":" + str(others_for_best[key]))
    # this wont work if we have to wrap around to get to the 200th, or if there are multiple asteroids at the 200th spot
    if counter == 200:
        part2 = others_for_best[key][0][1] * 100 + others_for_best[key][0][0]
    counter += 1

print("Part 1 = " + str(max_visible))
print("Part 2 = " + str(part2))