with open("input23.txt") as f:
    content = f.readlines()

part1 = 0
cards = {}
for cur_line in content:
    if cur_line == '\n':
        continue

    if cur_line[:-3] == "Player ":
        cur_player = int(cur_line[-3:-2])
        continue

    if cur_player not in cards:
        cards[cur_player] = []
    cards[cur_player].append(int(cur_line))

def min_deck():
    min = len(cards[1])
    for deck in cards:
        if len(cards[deck]) < min:
            min = len(cards[deck])
    return min

def play_round():
    if cards[1][0] > cards[2][0]: #p1 wins
        cards[1].append(cards[1][0])
        cards[1].append(cards[2][0])
    else:
        cards[2].append(cards[2][0])
        cards[2].append(cards[1][0])
    del cards[1][0]
    del cards[2][0]


while min_deck() > 0:
    play_round()

for cur_player in cards:
    if len(cards[cur_player]) > 0:
        for indx, cur_card in enumerate(cards[cur_player]):
            part1 += (len(cards[cur_player]) - indx) * cur_card

print(min_deck())
print("part 1 = " + str(part1))