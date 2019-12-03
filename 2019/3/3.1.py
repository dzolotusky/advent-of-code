with open("input3.txt") as f:
    content = f.readlines()

wires = []
wires.append(content[0].split(","))
wires.append(content[1].split(","))

grid = []
for i in range(0, 10000):
    sub_array = [None] * (10000)
    grid.append(sub_array)

cur_loc = (0,0)
cur_dir = (0, 0)
both_visited = []

for i in [0,1]:
    cur_loc = (0,0)
    for dir in wires[i]:
        if dir[0] == 'R':
            cur_dir = (1,0)
        else:
            if dir[0] == 'L':
                cur_dir = (-1,0)
            else:
                if dir[0] == 'U':
                    cur_dir = (0, 1)
                else:
                    if dir[0] == 'D':
                        cur_dir = (0, -1)

        steps = int(dir[1:])
        for step in range(steps):
            cur_loc = (cur_loc[0] + cur_dir[0],cur_loc[1] + cur_dir[1])

            if i == 1 and grid[cur_loc[0]][cur_loc[1]] != None:
                both_visited.append(cur_loc)

            if i == 0:
                grid[cur_loc[0]][cur_loc[1]] = 1

#            if i == 1:
#                visited_by_two.append(cur_loc)


#print("one = " + str(visited_by_one))
#print("two = " + str(visited_by_two))
print("both = " + str(both_visited))
min_dist = both_visited[0][0] + both_visited[0][1]
for loc in both_visited:
    dist = abs(loc[0]) + abs(loc[1])
    if dist < min_dist:
        min_dist = dist

print("part 1 = " + str(min_dist))
