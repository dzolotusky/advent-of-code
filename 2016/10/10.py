with open("input10.txt") as f:
    content = f.readlines()

bots = {}
bins = {}


def give_bot(value, bot_num):
    if bot_num in bots:
        bot = bots[bot_num]
    else:
        bot = {"holding": []}
        bots[bot_num] = bot

    bot["holding"].append(value)


def instruct_bot(low, high, bot_num):
    if bot_num in bots:
        bot = bots[bot_num]
    else:
        bot = {"holding": []}
        bots[bot_num] = bot

    bot["low"] = low
    bot["high"] = high


for cur_line in content:
    cur_line_split = cur_line.strip().split(' ')
    if cur_line[0] == 'v':
        give_bot(int(cur_line_split[1]), int(cur_line_split[-1]))
    else:
        instruct_bot(cur_line_split[5][0] + ":" + cur_line_split[6], cur_line_split[-2][0] + ":" + cur_line_split[-1],
                     int(cur_line_split[1]))


def total_holding():
    tot_holding = 0
    for cur_bot_num in bots:
        cur_bot = bots[cur_bot_num]
        cur_holding = cur_bot["holding"]
        tot_holding += len(cur_holding)

    return tot_holding


def add_to_bin(bin_num, value):
    print("adding " + str(bin_num) + " " + str(value))
    if bin_num in bins:
        bins[bin_num].append(value)
    else:
        bins[bin_num] = [value]


part1 = None
while total_holding() > 0:
    for cur_bot_num in bots:
        cur_bot = bots[cur_bot_num]
        cur_holding = cur_bot["holding"]
        if len(cur_holding) == 2:
            if 61 in cur_holding and 17 in cur_holding:
                part1 = cur_bot_num
                print("Part 1 = bot " + str(part1))

            cur_holding.sort()
            if cur_bot["low"][0] == 'o':
                add_to_bin(int(cur_bot["low"][2:]), cur_holding[0])
            else:
                bots[int(cur_bot["low"][2:])]["holding"].append(cur_holding[0])

            if cur_bot["high"][0] == 'o':
                add_to_bin(int(cur_bot["high"][2:]), cur_holding[1])
            else:
                bots[int(cur_bot["high"][2:])]["holding"].append(cur_holding[1])

            cur_bot["holding"] = []

print("Part 1 = bot " + str(part1))
print("Part 2 = " + str(bins[0][0] * bins[1][0] * bins[2][0]))
