# initial = "10000"
# goal_length = 20

initial = "10111011111001111"
goal_length = 35651584


def fill_data(a):
    b = a[::-1]
    b = "".join([str(int(b_val) ^ 1) for b_val in b])
    a = a + "0" + b
    return a


def get_checksum(data):
    checksum = []
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            checksum.append("1")
        else:
            checksum.append("0")
    if len(checksum) % 2 == 0:
        return get_checksum(checksum)
    else:
        return checksum


data = initial
while len(data) < goal_length:
    data = fill_data(data)

data = data[0:goal_length]
part1 = "".join(get_checksum(data))
print("checksum = " + str(part1))
