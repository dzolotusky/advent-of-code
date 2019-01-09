time_goal = 2503  # second at which we want to know the winner

with open("input14.txt") as f:
    content = f.readlines()

deer = []

for cur_line in content:
    cur_line_split = cur_line.split(" ")
    name = cur_line_split[0]
    speed = int(cur_line_split[3])
    flight_time = int(cur_line_split[6])
    rest_time = int(cur_line_split[-2])
    deer.append((speed, flight_time, rest_time, name))

deer_points = [0] * len(deer)
for minute in range(1, 1 + time_goal):
    deer_distance = [0] * len(deer)
    for i, cur_deer in enumerate(deer):
        speed = cur_deer[0]
        flight_time = cur_deer[1]
        rest_time = cur_deer[2]
        distance = int(minute / (flight_time + rest_time)) * (speed * flight_time)
        # above is only distance covered by full rest + flight periods
        remaining_time = minute % (flight_time + rest_time)
        if remaining_time < flight_time:
            distance = distance + remaining_time * speed
        else:
            distance = distance + flight_time * speed

        deer_distance[i] = distance
    max_dist = max(deer_distance)
    for i, dist in enumerate(deer_distance):
        if (dist == max_dist):
            deer_points[i] = deer_points[i] + 1

print(max(deer_points))
