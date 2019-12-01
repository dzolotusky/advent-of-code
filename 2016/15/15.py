with open("input15.txt") as f:
    content = f.readlines()

discs = []

for cur_line in content:
    cur_line_split = cur_line.strip().split(' ')
    disc_num = int(cur_line_split[1][1:])
    tot_positions = int(cur_line_split[3])
    start_pos = int(cur_line_split[-1][:-1])
    discs.append({"num": disc_num, "tot_pos": tot_positions, "cur_pos": start_pos})

for i in range(90000000):
    falls_through = True
    for disc in discs:
        disc["cur_pos"] += 1
        disc["cur_pos"] %= disc["tot_pos"]
        if (disc["cur_pos"] + disc["num"]) % disc["tot_pos"] != 0:
            falls_through = False

    if falls_through:
        print("part 1 = " + str(i + 1))
        exit()