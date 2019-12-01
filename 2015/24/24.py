with open("input24.txt") as f:
    content = f.readlines()

total = 0
containers = []
for cur_line in content:
    cur_weight = int(cur_line)
    containers.append(cur_weight)
    total += cur_weight

group_weight = int(total / 4)  # 3 for part 1, 4 for part 2

all_options = []
all_option_lengths = []
shortest = None


def get_all_combinations(selected, options):
    global all_options
    global shortest
    cur_total = sum(selected)
    if cur_total == group_weight:
        if shortest is None or len(selected) < shortest:
            shortest = len(selected)
        else:
            return 1
        all_options.append(selected)
        all_option_lengths.append(len(selected))
        return 1

    if cur_total > group_weight:
        return 0

    combos = 0
    for opt in options.copy():
        options.remove(opt)
        next_selected = selected.copy()
        next_selected.append(opt)
        if shortest is None or len(selected) <= shortest:
            combos = combos + get_all_combinations(next_selected, options.copy())

    return combos


get_all_combinations([], containers)

# print(all_options)
min_length = min(all_option_lengths)
# print(min_length)

combos_with_min_length = []
for combo in all_options:
    if len(combo) == min_length:
        combos_with_min_length.append(combo)

# print(combos_with_min_length)
min_qe = None
for combo in combos_with_min_length:
    qe = 1
    for w in combo:
        qe = qe * w
    if min_qe is None or qe < min_qe:
        min_qe = qe

print(min_qe)
