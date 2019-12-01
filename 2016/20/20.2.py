with open("input20.txt") as f:
    content = f.readlines()

max_ip = 4294967295
#max_ip = 9

ranges = []
for cur_line in content:
    ranges.append([int(val) for val in cur_line.split('-')])

ranges.sort(key=lambda n: (n[0]))

range_indx = 0
while range_indx < len(ranges) - 1:
    if ranges[range_indx][1] >= ranges[range_indx + 1][0]:
        if ranges[range_indx][1] <= ranges[range_indx + 1][1]:
            ranges[range_indx][1] = ranges[range_indx + 1][1]
        del ranges[range_indx + 1]
        range_indx = 0
    else:
        range_indx += 1

print(ranges)

range_indx = 0
allowed_ips = 0
for range_indx in range(len(ranges) - 1):
    top = min(max_ip, ranges[range_indx + 1][0])
    delta = top - ranges[range_indx][1] - 1
    if delta > 0:
        allowed_ips += delta
        print(str(ranges[range_indx][1]) + " - " + str(top) + ": " + str(delta))

if ranges[-1][1] < max_ip:
    allowed_ips += max_ip - ranges[-1][1]
    print(str(ranges[-1][1]) + " - " + str(max_ip) + ": " + str(max_ip - ranges[-1][1]))

print("part 2 = " + str(allowed_ips))

# 771316128 too high
# 7965257480 too high

#M4294967295
#  771316128