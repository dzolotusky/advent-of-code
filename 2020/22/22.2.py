with open("input22.txt") as f:
    content = f.readlines()

part2 = 0
all_cards = {}
for cur_line in content:
    if cur_line == '\n':
        continue

    if cur_line[:-3] == "Player ":
        cur_player = int(cur_line[-3:-2])
        continue

    if cur_player not in all_cards:
        all_cards[cur_player] = []
    all_cards[cur_player].append(int(cur_line))


def min_deck(test_cards):
    min_deck_size = len(test_cards[1])
    for deck in test_cards:
        if len(test_cards[deck]) < min_deck_size:
            min_deck_size = len(test_cards[deck])
    return min_deck_size


def play_round(hands):
    # check for recursive hand
    if len(hands[1]) >= 1 + hands[1][0] and len(hands[2]) >= 1 + hands[2][0]:
        new_hands = {1: hands[1].copy()[1:hands[1][0] + 1], 2: hands[2].copy()[1:hands[2][0] + 1]}
        new_hands = play_game(new_hands)
        if len(new_hands[1]) == 0:
            winner = 2
        else:
            winner = 1
    else:
        if hands[1][0] > hands[2][0]:
            winner = 1
        else:
            winner = 2

    return winner


def play_game(cards):
    previous_hands = []
    while min_deck(cards) > 0:
        if cards in previous_hands:
            winner = 1
            cards[winner].append(cards[winner][0])
            cards[winner].append(cards[2 if winner == 1 else 1][0])
            del cards[1][0]
            del cards[2][0]
            break
        else:
            previous_hands.append({1: cards[1].copy(), 2: cards[2].copy()})
            winner = play_round(cards)

        cards[winner].append(cards[winner][0])
        cards[winner].append(cards[2 if winner == 1 else 1][0])
        del cards[1][0]
        del cards[2][0]

    return cards


all_cards = play_game(all_cards)
for cur_player in all_cards:
    if len(all_cards[cur_player]) > 0:
        for indx, cur_card in enumerate(all_cards[cur_player]):
            part2 += (len(all_cards[cur_player]) - indx) * cur_card

print("part 2 = " + str(part2))
