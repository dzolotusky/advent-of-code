with open("input13.txt") as f:
    content = f.readlines()

guests = []
happiness_deltas = {}

for cur_line in content:
    cur_line_split = cur_line.split(" ")
    name1 = cur_line_split[0]
    name2 = cur_line_split[-1][:-2]
    if cur_line_split[2][0] == "g":
        delta = int(cur_line_split[3])
    else:
        delta = int(cur_line_split[3]) * -1
    if (name2, name1) in happiness_deltas:
        old_delta = happiness_deltas[(name2, name1)]
        happiness_deltas[(name2, name1)] = delta + old_delta
    else:
        happiness_deltas[(name1, name2)] = delta

    if name1 not in guests:
        guests.append(name1)


def get_happiness(seats):
    happiness = 0
    for i in range(len(seats)):
        pair = (seats[i], seats[(i + 1) % len(seats)])
        if not pair in happiness_deltas:
            pair = (pair[1], pair[0])
        happiness = happiness + happiness_deltas[pair]
    return happiness


def get_all_permutations(options):
    if len(options) == 1:
        return [options]

    permutations = []
    for opt in options:
        next_options = options.copy()
        next_options.remove(opt)
        for permutation in get_all_permutations(next_options):
            permutations.append([opt] + permutation)

    return permutations


max_happiness = 0
for perm in get_all_permutations(guests):
    cur_happiness = get_happiness(perm)
    if get_happiness(perm) > max_happiness:
        max_happiness = cur_happiness

print("part 1 = " + str(max_happiness))
