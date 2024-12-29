with open("test_input21.txt") as f:
    content = f.readlines()

part2 = 0
player_positions = []
player_scores = (0,0)
possible_rolls = [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]

for cur_line in content:
    cur_line_split = cur_line.split()
    start_pos = int(cur_line_split[-1])
    player_positions.append(start_pos)

player_positions = tuple(player_positions)
cache = {}


def play(p_num, player_pos, player_score):
    if max(player_score) >= 21:
        if player_score[0] >= 21:
            return [1, 0]
        else:
            return [0, 1]

    next_turn = (p_num + 1) % 2
    cur_pos = player_pos[p_num]
    outcomes = [0, 0]
    for cur_roll in possible_rolls:
        next_pos = (cur_pos + cur_roll) % 10
        if next_pos == 0:
            next_pos = 10

        new_score = list(player_score)
        new_score[p_num] += next_pos
        new_score = tuple(new_score)
        new_pos = list(player_pos)
        new_pos[p_num] = next_pos
        new_pos = tuple(new_pos)
        if (next_turn, new_pos, new_score) in cache:
            sub_outcomes = cache[(next_turn, new_pos, new_score)]
        else:
            sub_outcomes = play(next_turn, new_pos, new_score)
            cache[(next_turn, new_pos, new_score)] = sub_outcomes
        outcomes[0] += sub_outcomes[0]
        outcomes[1] += sub_outcomes[1]

    return outcomes


part2 = play(0, player_positions, player_scores)
part2 = max(part2)
print("part 2 = " + str(part2))