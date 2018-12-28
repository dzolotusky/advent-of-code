with open("input6.txt") as f:
    content = f.readlines()

lights = []
brightness = []

for i in range(0,1000):
    sub_array = [0]*1000
    lights.append(sub_array)

for i in range(0,1000):
    sub_array = [0]*1000
    brightness.append(sub_array)

def read_loc(loc_string):
    loc_string_split = [int(coord) for coord in loc_string.split(",")]
    return loc_string_split[0], loc_string_split[1]

for cur_line in content:
    cur_line_split = cur_line.split(" ")

    end_loc = read_loc(cur_line_split[-1])
    if cur_line_split[0] == "turn":
        if cur_line_split[1] == "on":
            new_state = 1
        else:
            new_state = 0
        start_loc = read_loc(cur_line_split[2])
        for i in range(start_loc[0], end_loc[0] + 1):
            for j in range(start_loc[1], end_loc[1] + 1):
                lights[i][j] = new_state
                if new_state:
                    brightness[i][j] = brightness[i][j] + 1
                else:
                    if brightness[i][j] > 0:
                        brightness[i][j] = brightness[i][j] - 1
    else:
        start_loc = read_loc(cur_line_split[1])
        for i in range(start_loc[0], end_loc[0] + 1):
            for j in range(start_loc[1], end_loc[1] + 1):
                lights[i][j] = (lights[i][j] + 1) % 2
                brightness[i][j] = brightness[i][j] + 2


lights_on = 0
for i in range(len(lights)):
    for j in range(len(lights[i])):
        lights_on = lights_on + lights[i][j]

tot_brightness = 0
for i in range(len(brightness)):
    for j in range(len(brightness[i])):
        tot_brightness = tot_brightness + brightness[i][j]

print("Part 1 = " + str(lights_on))
print("Part 2 = " + str(tot_brightness))

# 14190938 too low
#