with open("input19.txt") as f:
    content = f.readlines()

replacements = {}

line_num = 0
cur_line = None
cur_line = content[line_num]
while cur_line != "\n":
    cur_line_split = cur_line.split(" ")
    initial_val = cur_line_split[0].strip()
    replaced_val = cur_line_split[2].strip()
    if initial_val in replacements:
        replacements[initial_val].append(replaced_val)
    else:
        replacements[initial_val] = [replaced_val]

    line_num = line_num + 1
    cur_line = content[line_num]

molecule = content[line_num + 1]

potentials = []
for repl in replacements:
    if repl in molecule:
        sub_molecule = molecule
        cur_index = 0
        while repl in sub_molecule[cur_index:]:
            cur_index = sub_molecule.index(repl, cur_index)
            for new_chars in replacements[repl]:
                potentials.append(sub_molecule[:cur_index] + sub_molecule[cur_index:].replace(repl, new_chars, 1))
            cur_index = len(repl) + cur_index

print(str(len(potentials)) + " total replacements")
print(str(len(set(potentials))) + " distinct molecules")
