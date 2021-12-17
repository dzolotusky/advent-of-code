with open("input17.txt") as f:
    content = f.readlines()

target_string = content[0]
target_x = [int(n) for n in target_string[target_string.find("x=") + 2:target_string.find(",")].split("..")]
target_y = [int(n) for n in target_string[target_string.find("y=") + 2:].split("..")]


x_cache = {}


def x_at_time(t, x_velocity):
    if (t, x_velocity) in x_cache:
        return x_cache[(t, x_velocity)]

    cur_x = 0
    cur_velocity = x_velocity
    for cur_t in range(t):
        cur_x += cur_velocity
        if cur_velocity < 0:
            cur_velocity += 1
        else:
            if cur_velocity > 0:
                cur_velocity -= 1

    x_cache[(t, x_velocity)] = cur_x
    return cur_x


y_cache = {}


def y_at_time(t, y_velocity):
    if (t, y_velocity) in y_cache:
        return y_cache[(t, y_velocity)]

    cur_y = 0
    cur_velocity = y_velocity
    for cur_t in range(t):
        cur_y += cur_velocity
        cur_velocity -= 1

    y_cache[(t, y_velocity)] = cur_y
    return cur_y


max_y = 0
max_y_xs = []
max_y_on_flight = 0
initial_values_that_hit = []
for x_vel_test in range(target_x[1] + 1):
    for y_vel_test in range(target_y[0], -1 * target_y[0]):
        max_y_here = 0
        for t_test in range(2000):
            cur_x = x_at_time(t_test, x_vel_test)
            if cur_x > target_x[1]:
                break

            cur_y = y_at_time(t_test, y_vel_test)
            if cur_y < target_y[0]:
                break

            if cur_y > max_y_here:
                max_y_here = cur_y
            if target_x[0] <= cur_x <= target_x[1]:
                if target_y[0] <= cur_y <= target_y[1]:
                    initial_values_that_hit.append((x_vel_test, y_vel_test))
                    if max_y_here > max_y_on_flight:
                        max_y = y_vel_test
                        max_y_xs.append((x_vel_test))
                        max_y_on_flight = max_y_here
                    break

part1 = max_y_on_flight
part2 = len(initial_values_that_hit)
print("part 1 = " + str(part1))
print("part 2 = " + str(part2))