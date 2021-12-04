with open("input4.txt") as f:
    content = f.readlines()

numbers_called = [int(n) for n in content[0].split(",")]
boards = []
cur_board = None

for cur_line in content[1:]:
    if cur_line == "\n":
        if cur_board is not None:
            boards.append(cur_board)
        cur_board = []
        continue

    cur_board.append([int(n) for n in cur_line.strip().split()])
boards.append(cur_board)


def find_winners():
    winners = []
    winner_sum = -1
    for cur_board in boards:
        for i in range(len(cur_board)):
            if cur_board[i] == ['x','x','x','x','x'] or (cur_board[0][i] == 'x' and cur_board[1][i] == 'x' and cur_board[2][i] == 'x' and cur_board[3][i] == 'x' and cur_board[4][i] == 'x'):
                winners.append(cur_board)
                winner_sum = 0
                for winner_i in range(len(cur_board)):
                    for winner_j in range(len(cur_board[winner_i])):
                        winner_sum += 0 if cur_board[winner_i][winner_j] == 'x' else cur_board[winner_i][winner_j]

    return winners, winner_sum


for called_num in numbers_called:
    for cur_board in boards:
        for i in range(len(cur_board)):
            for j in range(len(cur_board[i])):
                if cur_board[i][j] == called_num:
                    cur_board[i][j] = 'x'
    (winner_boards, winner_sum) = find_winners()
    if winner_sum != -1:
        if len(boards) > 1:
            boards = [board for board in boards if board not in winner_boards]
        else:
            break;

part2 = winner_sum * called_num

print("part 2 = " + str(part2))