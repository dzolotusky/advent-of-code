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


def find_winner():
    for cur_board in boards:
        for i in range(len(cur_board)):
            if cur_board[i] == ['x','x','x','x','x'] or (cur_board[0][i] == 'x' and cur_board[1][i] == 'x' and cur_board[2][i] == 'x' and cur_board[3][i] == 'x' and cur_board[4][i] == 'x'):
                winner_sum = 0
                for winner_i in range(len(cur_board)):
                    for winner_j in range(len(cur_board[winner_i])):
                        winner_sum += 0 if cur_board[winner_i][winner_j] == 'x' else cur_board[winner_i][winner_j]
                return winner_sum
    return -1


for called_num in numbers_called:
    for cur_board in boards:
        for i in range(len(cur_board)):
            for j in range(len(cur_board[i])):
                if cur_board[i][j] == called_num:
                    cur_board[i][j] = 'x'
    winner = find_winner()
    if winner != -1:
        break;

part1 = winner * called_num

print("part 1 = " + str(part1))