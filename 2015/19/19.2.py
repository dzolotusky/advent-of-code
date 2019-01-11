with open("input19.txt") as f:
    content = f.readlines()

replacements = {}

line_num = 0
cur_line = content[line_num]
while cur_line != "\n":
    initial_val, replaced_val = cur_line.split(" => ")
    rep_val = replaced_val.strip()
    if initial_val in replacements:
        replacements[initial_val].append(replaced_val.strip())
    else:
        replacements[initial_val] = [replaced_val.strip()]

    line_num = line_num + 1
    cur_line = content[line_num]

goal_molecule = 'e'
replacement_keys = list(replacements.keys())
# replace longest matching substring. This doesn't work for the sample input, but does for the real input...
replacement_keys.sort(key=lambda k: len(k), reverse=True)

cur_molecule = content[line_num + 1]
steps = 0

while len(cur_molecule) >= 1:
    mol_len = len(cur_molecule)
    if cur_molecule == goal_molecule:
        print("done")
        print("steps = " + str(steps))
        exit()

    for cur in replacement_keys:
        for rep in replacements[cur]:
            if rep in cur_molecule:
                cur_molecule = cur_molecule.replace(rep, cur, 1)
                steps += 1
                break

print(cur_molecule)
print("failed")
