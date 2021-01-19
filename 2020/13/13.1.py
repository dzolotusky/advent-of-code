import sys

with open("input13.txt") as f:
    content = f.readlines()

part1 = 0
earliest = int(content[0])
buses = content[1].split(",")
buses = list(filter(lambda bus: bus != "x", buses))
buses = [int(bus_str) for bus_str in buses]
next_bus = buses[0]
wait_time = sys.maxsize

for cur_bus in buses:
    cur_wait_time = ((int(earliest / cur_bus) + 1) * cur_bus) - earliest
    print(cur_wait_time)
    if cur_wait_time < wait_time:
        next_bus = cur_bus
        wait_time = cur_wait_time
part1 = wait_time * next_bus

print("part 1 = " + str(part1))