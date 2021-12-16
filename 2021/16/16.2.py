import math

with open("input16.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
input = (bin(int(content[0].strip(), 16))[2:].zfill(len(content[0].strip()) * 4))


def read_packet_id(packet):
    return int(packet[3:6], 2)


def read_packet_version(packet):
    return int(packet[:3], 2)


def do_operation(packet_id, sub_packet_data):
    if packet_id == 0:
        return sum(sub_packet_data)
    if packet_id == 1:
        return math.prod(sub_packet_data)
    if packet_id == 2:
        return min(sub_packet_data)
    if packet_id == 3:
        return max(sub_packet_data)
    if packet_id == 5:
        if len(sub_packet_data) != 2:
            print("greater than packet of length " + str(len(sub_packet_data)))
        else:
            return 1 if sub_packet_data[0] > sub_packet_data[1] else 0
    if packet_id == 6:
        if len(sub_packet_data) != 2:
            print("less than packet of length " + str(len(sub_packet_data)))
        else:
            return 1 if sub_packet_data[0] < sub_packet_data[1] else 0
    if packet_id == 7:
        if len(sub_packet_data) != 2:
            print("equal packet of length " + str(len(sub_packet_data)))
        else:
            return 1 if sub_packet_data[0] == sub_packet_data[1] else 0


def read_packet(packet):
    global part1
    value = None
    packet_length = 0
    p_ver = read_packet_version(packet)
    part1 += p_ver
    packet_id = read_packet_id(packet)
    if packet_id != 4:
        l_type_id = int(packet[6], 2)
        sub_packet_data = []
        if l_type_id == 0:
            length = int(packet[8:22], 2)
            cur_loc = 0
            while cur_loc < length:
                [data, size] = read_packet(packet[cur_loc + 22:])
                sub_packet_data.append(data)
                cur_loc += size
            packet_length = 22 + length
        else:
            if l_type_id == 1:
                num_sub_packets = int(packet[8:18], 2)
                sub_packets = 0
                cur_loc = 0
                while sub_packets < num_sub_packets:
                    [data, size] = read_packet(packet[cur_loc + 18:])
                    sub_packet_data.append(data)
                    cur_loc += size
                    sub_packets += 1
                packet_length = 18 + cur_loc
            else:
                print("invalid length_type_id: " + str(l_type_id))
                exit(0)

        value = do_operation(packet_id, sub_packet_data)

        if packet_id == 0:
            op = "sum"
        if packet_id == 1:
            op = "prod"
        if packet_id == 2:
            op = "min"
        if packet_id == 3:
            op = "max"
        if packet_id == 5:
            op = "greater"
        if packet_id == 6:
            op = "less"
        if packet_id == 7:
            op = "equal"
        print(str(value) + " = " + op + " " + str(sub_packet_data))

    if packet_id == 4:
        number_str = ""
        cur_loc = 6
        while packet[cur_loc] == "1":
            number_str += packet[cur_loc + 1:cur_loc + 5]
            cur_loc += 5

        number_str += packet[cur_loc + 1:cur_loc + 5]
        packet_length = cur_loc + 5
        value = int(number_str, 2)

    return value, packet_length


part2 = read_packet(input)[0]

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))