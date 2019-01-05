time_goal = 2503 #1000 #second at which we want to know the winner

with open("input14.txt") as f:
    content = f.readlines()

deer = {}

for cur_line in content:
    cur_line_split = cur_line.split(" ")
    name = cur_line_split[0]
    speed = int(cur_line_split[3])
    flight_time = int(cur_line_split[6])
    rest_time = int(cur_line_split[-2])
    print(name + ":" + str(speed) + " for " + str(flight_time) + " rest " + str(rest_time))
    deer[name] = (speed, flight_time, rest_time)

for cur_deer in deer:
    speed = deer[cur_deer][0]
    flight_time = deer[cur_deer][1]
    rest_time = deer[cur_deer][2]
    distance = int(time_goal / (flight_time + rest_time)) * (speed * flight_time)
    # above is only distance covered by full rest + flight periods
    remaining_time = time_goal % (flight_time + rest_time)
    if remaining_time < flight_time:
        distance = distance + remaining_time * speed
    else:
        distance = distance + flight_time * speed

    print(cur_deer + ":" + str(distance))