with open("input7.txt") as f:
    content = f.readlines()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

wires = {}
for cur_line in content:
    value_and_wire = [val.rstrip().lstrip() for val in cur_line.split("->")]
    wire = value_and_wire[-1].lstrip().rstrip()
    value = [int(val) if is_int(val) else val for val in value_and_wire[0].split(" ")]

    if len(value) == 1:
        if is_int(value[0]):
            wires[wire] = int(value[0])
        else:
            wires[wire] = value[0]
    else:
        wires[wire] = value

def get_value(value_str):
    if is_int(value_str):
        return int(value_str)
    else:
        return wires[value_str]

for i in range(1,110):
    for wire in wires:
        if isinstance(wires[wire], list):
            cur_wire = wires[wire]
            if len(cur_wire) == 2:  # NOT
                if isinstance(wires[cur_wire[1]], list):  # value is not resolved yet
                    continue
                else:
                    wires[wire] = ~wires[cur_wire[1]]

            if len(cur_wire) == 3:
                if isinstance(cur_wire[0], str) and isinstance(wires[cur_wire[0]], list):  # value is not resolved yet
                    continue

                if cur_wire[1] == "LSHIFT":
                    wires[wire] = wires[cur_wire[0]] << int(cur_wire[2])
                    continue
                if cur_wire[1] == "RSHIFT":
                    wires[wire] = wires[cur_wire[0]] >> int(cur_wire[2])
                    continue

                if isinstance(wires[cur_wire[2]], list):  # value is not resolved yet
                    continue

                values = (get_value(cur_wire[0]), get_value(cur_wire[2]))
                if cur_wire[1] == "AND":
                    wires[wire] = values[0] & values[1]
                else:
                    if cur_wire[1] == "OR":
                        wires[wire] = values[0] | values[1]

        if isinstance(wires[wire], str):
            wires[wire] = wires[wires[wire]]

        if isinstance(wires[wire], int):
            if wires[wire] < 0:
                wires[wire] = wires[wire] + 65536


def print_wires():
    wire_names = list(wires.keys())
    wire_names.sort()
    for wire_name in wire_names:
        print(wire_name + ": " + str(wires[wire_name]))

print_wires()

# test answers:
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

#: 16076