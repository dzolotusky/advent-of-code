with open("input21.txt") as f:
    content = f.readlines()

part1 = 0
player_pos = []
player_score = [0,0]
die_next = 1
die_rolls = 0
for cur_line in content:
    cur_line_split = cur_line.split()
    start_pos = int(cur_line_split[-1])
    player_pos.append(start_pos)


def take_turn(p_num):
    global die_next, die_rolls
    cur_pos = player_pos[p_num]
    rolls = 3 * die_next + 3
    die_rolls += 3
    die_next += 3
    next_pos = (cur_pos + rolls) % 10
    if next_pos == 0:
        next_pos = 10
    player_score[p_num] += next_pos
    player_pos[p_num] = next_pos


next_turn = 0
while player_score[0] < 1000 and player_score[1] < 1000:
    take_turn(next_turn)
    next_turn = (next_turn + 1) % 2

loser_score = min(player_score)
part1 = loser_score * die_rolls
print("part 1 = " + str(part1))