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
combined_steps = []

for i in [0,1]:
    num_steps = 0
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
            num_steps += 1
            cur_loc = (cur_loc[0] + cur_dir[0],cur_loc[1] + cur_dir[1])

            if i == 1 and grid[cur_loc[0]][cur_loc[1]] != None:
                both_visited.append(cur_loc)
                combined_steps.append(num_steps + grid[cur_loc[0]][cur_loc[1]])

            if i == 0:
                grid[cur_loc[0]][cur_loc[1]] = num_steps

print("both = " + str(combined_steps))

min_dist =  combined_steps[0]
for steps in combined_steps:
    if steps < min_dist:
        min_dist = steps
print ("part 2 = " + str(min_dist))
