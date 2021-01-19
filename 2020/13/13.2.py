from functools import reduce

with open("input13.txt") as f:
    content = f.readlines()

part2 = 0
bus_nums = content[1].split(",")
buses = []

for bus_index in range(len(bus_nums)):
    if (bus_nums[bus_index] != "x"):
        buses.append((int((bus_nums[bus_index])), bus_index))

print(buses)

## start https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

## end https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
n = []
a = []

for bus in buses:
    n.append(bus[0])
    a.append(bus[1] * -1)

rem = chinese_remainder(n, a)
part2 = rem

print("part 2 = " + str(part2))