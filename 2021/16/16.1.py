with open("input16.txt") as f:
    content = f.readlines()

part1 = 0
input = (bin(int(content[0].strip(), 16))[2:].zfill(len(content[0].strip()) * 4))


def read_packet_id(packet):
    return int(packet[3:6], 2)


def read_packet_version(packet):
    return int(packet[:3], 2)


def read_packet(packet):
    global part1
    packet_length = 0
    p_ver = read_packet_version(packet)
    part1 += p_ver
    packet_id = read_packet_id(packet)
    if packet_id != 4:
        l_type_id = int(packet[6], 2)
        if l_type_id == 0:
            length = int(packet[8:22], 2)
            cur_loc = 0
            while cur_loc < length:
                [data, len] = read_packet(packet[cur_loc + 22:])
                cur_loc += len
            packet_length = 22 + length
        else:
            if l_type_id == 1:
                num_sub_packets = int(packet[8:18], 2)
                sub_packets = 0
                cur_loc = 0
                while sub_packets < num_sub_packets:
                    [data, len] = read_packet(packet[cur_loc + 18:])
                    cur_loc += len
                    sub_packets += 1
                packet_length = 18 + cur_loc
            else:
                print("invalid length_type_id: " + str(l_type_id))
                exit(0)

    if packet_id == 4:
        number_str = ""
        cur_loc = 6
        while packet[cur_loc] == "1":
            number_str += packet[cur_loc:cur_loc + 5]
            cur_loc += 5

        number_str += packet[cur_loc:cur_loc + 5]
        packet_length = cur_loc + 5

    return (None, packet_length)


read_packet(input)

print("part 1 = " + str(part1))
