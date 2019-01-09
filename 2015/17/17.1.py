total_eggnog = 150 #25

with open("input17.txt") as f:
    content = f.readlines()

containers = []
for cur_line in content:
    containers.append(int(cur_line))

def get_all_combinations(selected, options):
    cur_total = sum(selected)
    if cur_total == total_eggnog:
#        print(selected)
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

print(get_all_combinations([], containers))