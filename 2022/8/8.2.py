with open("input8.txt") as f:
    content = f.readlines()

part2 = 0
grid = []
scenic_scores = []

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    scenic_scores.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = int(content[i][j])
        scenic_scores[i][j] = 0

def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


def print_scores():
    for i in range(len(scenic_scores)):
        for j in range(len(scenic_scores[i])):
            print(scenic_scores[i][j], end=',')
        print()


def calc_score(x: int, y: int):
    dir_scores = []
    score = 1
    cur_height = grid[x][y]
    dir_score = 0
    for i in range(x + 1, len(grid)):
        dir_score += 1
        if grid[i][y] >= cur_height:
            break

    dir_scores.append(dir_score)
    dir_score = 0
    for i in range(x - 1, -1, -1):
        dir_score += 1
        if grid[i][y] >= cur_height:
            break

    dir_scores.append(dir_score)
    dir_score = 0
    for j in range(y + 1, len(grid[x])):
        dir_score += 1
        if grid[x][j] >= cur_height:
            break

    dir_scores.append(dir_score)
    dir_score = 0
    for j in range(y - 1, -1, -1):
        dir_score += 1
        if grid[x][j] >= cur_height:
            break

    dir_scores.append(dir_score)

    for cur_score in dir_scores:
        if cur_score > 0:
            score *= cur_score

    return score

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        scenic_scores[i][j] = calc_score(i, j)

for i in range(len(scenic_scores)):
    part2 = max(part2, max(scenic_scores[i]))

print("part2 = " + str(part2))
