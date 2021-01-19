import math

with open("input14.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
mask = ""
mask_or = 0
mask_and = 1
mem = {}
mem2 = {}

for cur_line in content:
    cur_line_split = cur_line.split("=")
    if cur_line_split[0].strip() == "mask":
        mask = cur_line_split[1].lstrip().strip()
        mask_or = int(mask.replace("X", "0"), 2)
        mask_and = int(mask.replace("X", "1"), 2)
    else:
        mem_address = int(cur_line_split[0].split("[")[1][:-2])
        value = int(cur_line_split[1].lstrip().strip())
        mem2_addresses = [mem_address | mask_or]
        mem2_value = value
        value &= mask_and
        value |= mask_or
        mem[mem_address] = value

        for indx in range(len(mask)):
            if mask[indx] == "X":
                for address in mem2_addresses.copy():
                    another = address
                    x_place = int(math.pow(2, 35 - indx))
                    if another & x_place == 0:
                        another += x_place
                    else:
                        another -= x_place
                    mem2_addresses.append(another)

        for mem2_address in mem2_addresses:
            mem2[mem2_address] = mem2_value

part1 = sum(mem.values())
part2 = sum(mem2.values())

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))