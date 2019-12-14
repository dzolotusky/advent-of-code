with open("input12.txt") as f:
    content = f.readlines()

moon_locations = []
moon_velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

for cur_line in content:
    cur_line_split = cur_line.strip().strip(">").split(',')
    coords = []
    for line_piece in cur_line_split:
        coords.append(int(line_piece.split("=")[1]))
    moon_locations.append(coords)

print("initial locations = " + str(moon_locations))
print("initial velocities = " + str(moon_velocities))
steps = 1000000

initial_x = [moon_locations[0][0], moon_locations[1][0], moon_locations[2][0], moon_locations[3][0]]
initial_y = [moon_locations[0][1], moon_locations[1][1], moon_locations[2][1], moon_locations[3][1]]
initial_z = [moon_locations[0][2], moon_locations[1][2], moon_locations[2][2], moon_locations[3][2]]
same_x = []
same_y = []
same_z = []


for step_num in range(steps):
    for moon_index, cur_moon_loc in enumerate(moon_locations):
        other_moon_locations = moon_locations.copy()
        other_moon_locations.remove(cur_moon_loc)
        for other_moon in other_moon_locations:
            vel_delta = []
            for coord_index in range(3):
                if cur_moon_loc[coord_index] < other_moon[coord_index]:
                    vel_delta.append(1)
                else:
                    if cur_moon_loc[coord_index] > other_moon[coord_index]:
                        vel_delta.append(-1)
                    else:
                        if cur_moon_loc[coord_index] == other_moon[coord_index]:
                            vel_delta.append(0)
            new_velocity = (moon_velocities[moon_index][0] + vel_delta[0], moon_velocities[moon_index][1] + vel_delta[1], moon_velocities[moon_index][2] + vel_delta[2])
            moon_velocities[moon_index] = new_velocity

    for moon_index in range(4):
        moon_locations[moon_index] = (moon_locations[moon_index][0] + moon_velocities[moon_index][0],
                                      moon_locations[moon_index][1] + moon_velocities[moon_index][1],
                                      moon_locations[moon_index][2] + moon_velocities[moon_index][2])

#    print(str(step_num + 1) + " locations = " + str(moon_locations))
#    print(str(step_num + 1) + " velocities = " + str(moon_velocities))

    cur_x = [moon_locations[0][0], moon_locations[1][0], moon_locations[2][0], moon_locations[3][0]]
    cur_y = [moon_locations[0][1], moon_locations[1][1], moon_locations[2][1], moon_locations[3][1]]
    cur_z = [moon_locations[0][2], moon_locations[1][2], moon_locations[2][2], moon_locations[3][2]]
    if cur_x == initial_x:
        same_x.append(step_num + 1)
    #    print("X's equal: " + str(step_num + 1))
    if cur_y == initial_y:
        same_y.append(step_num + 1)
    #    print("Y's equal: " + str(step_num + 1))
    if cur_z == initial_z:
        same_z.append(step_num + 1)
    #    print("Z's equal: " + str(step_num + 1))

#print("final locations = " + str(moon_locations))
#print("final velocities = " + str(moon_velocities))

total_energy = 0
for moon_index in range(4):
    pot = abs(moon_locations[moon_index][0]) + abs(moon_locations[moon_index][1]) + abs(moon_locations[moon_index][2])
    kin = abs(moon_velocities[moon_index][0]) + abs(moon_velocities[moon_index][1]) + abs(moon_velocities[moon_index][2])
    moon_energy =  pot * kin
    #print("moon energy = " + str(moon_energy))
    total_energy += moon_energy

print("total energy = " + str(total_energy))

print ("x's = " + str(same_x))
print ("y's = " + str(same_y))
print ("z's = " + str(same_z))