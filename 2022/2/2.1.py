with open("input2.txt") as f:
    content = f.readlines()

my_score = 0

for cur_line in content:
    plays = cur_line.split()
    if plays[1] == "X":
        my_score += 1
        if plays[0] == "A":
            my_score += 3
        if plays[0] == "B":
            my_score += 0
        if plays[0] == "C":
            my_score += 6
    if plays[1] == "Y":
        my_score += 2
        if plays[0] == "A":
            my_score += 6
        if plays[0] == "B":
            my_score += 3
        if plays[0] == "C":
            my_score += 0
    if plays[1] == "Z":
        my_score += 3
        if plays[0] == "A":
            my_score += 0
        if plays[0] == "B":
            my_score += 6
        if plays[0] == "C":
            my_score += 3

part1 = my_score

print("part 1 = " + str(part1))
