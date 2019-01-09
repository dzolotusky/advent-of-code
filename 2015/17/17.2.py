total_eggnog = 150  # 25

with open("input17.txt") as f:
    content = f.readlines()

containers = []
for cur_line in content:
    containers.append(int(cur_line))

all_option_lenghts = []


def get_all_combinations(selected, options):
    global all_options
    cur_total = sum(selected)
    if cur_total == total_eggnog:
        all_option_lenghts.append(len(selected))
        return 1

    if cur_total > total_eggnog:
        return 0

    combos = 0
    for opt in options.copy():
        options.remove(opt)
        next_selected = selected.copy()
        next_selected.append(opt)
        combos = combos + get_all_combinations(next_selected, options.copy())

    return combos


get_all_combinations([], containers)

# print(all_option_lenghts)
min_length = min(all_option_lenghts)

num_at_min = 0
for cur_len in all_option_lenghts:
    if cur_len == min_length:
        num_at_min = num_at_min + 1

print("min = " + str(min_length))
print("num at min = " + str(num_at_min))
