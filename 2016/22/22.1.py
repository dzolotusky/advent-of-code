with open("input22.txt") as f:
    content = f.readlines()

nodes = []  # (name, used, avail)

for cur_line in content[2:]:
    cur_line_split = cur_line.strip().split()
    nodes.append((cur_line_split[0], int(cur_line_split[2][:-1]), int(cur_line_split[3][:-1])))

nodes_by_used = nodes
nodes_by_avail = nodes.copy()

nodes_by_avail.sort(key=lambda n: (n[2]), reverse=True)

nodes_by_used = [val for val in nodes_by_used if val[1] <= nodes_by_avail[0][2]]
nodes_by_used.sort(key=lambda n: (n[1]))

viable_pairs = 0
for used_node in nodes_by_used:
    for avail_node in nodes_by_avail:
        if 0 < used_node[1] <= avail_node[2]:
            if used_node[0] != avail_node[0]:
                viable_pairs += 1
        else:
            break

print("part 1 = " + str(viable_pairs))