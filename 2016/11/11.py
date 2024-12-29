import networkx as nx

with open("test_input.txt") as f:
    content = f.readlines()

floors = []
all_items = []
network_graph = nx.Graph()

for cur_line in content:
    cur_line_split = cur_line.strip().split(' ')
    cur_floor = []
    floors.append(cur_floor)
    if cur_line_split[4] == "nothing":
        continue

    floor_contents = cur_line_split[4:]
    while 'a' in floor_contents:
        floor_contents.remove('a')

    while 'and' in floor_contents:
        floor_contents.remove('and')

    word_index = 0
    while word_index < len(floor_contents):
        item = (floor_contents[word_index][0] + floor_contents[word_index + 1][0]).upper()
        cur_floor.append(item)
        all_items.append(item)
        word_index += 2

floors[0].append("E")
all_items.sort()


def print_floors(state, desc):
    print("----Printing---- " + str(desc))
    for index in range(len(state)):
        cur_floor_num = len(state) - index
        print("F" + str(cur_floor_num), end=' ')
        if "E" in state[cur_floor_num - 1]:
            print('E', end=' ')
        else:
            print('.', end=' ')

        for item in all_items:
            if item not in state[cur_floor_num - 1]:
                print(' . ', end='')
            else:
                print(' ' + item, end='')

        print(" ")


def is_valid_state(state):
    if state is None:
        return False

    for items_on_floor in state:
        for item in items_on_floor:
            if len(item) > 1 and item[1] == "M":
                for other_item in items_on_floor:
                    if len(other_item) > 1 and other_item[1] == "G" and item[0] == other_item[0]:
                        continue

                    if len(other_item) > 1 and other_item[1] == "G" and item[0] != other_item[0]:
                        return False
    return True


print_floors(floors, "initial")

initial_state = floors.copy()
visited_states = []
states_to_visit = [initial_state]
while len(states_to_visit) > 0:
    next_states = []
    for old_state in states_to_visit:
        visited_states.append(str(old_state))
        for floor_index, items_on_floor in enumerate(old_state):
            if "E" in items_on_floor:
                all_pairs = []
                for a in items_on_floor:
                    for b in items_on_floor:
                        if (b, a) not in all_pairs and a != "E" and b != "E":
                            all_pairs.append((a, b))
                all_pairs = [[a[0], None] if a[0] == a[1] else a for a in all_pairs]
                for cur_pair in all_pairs:
                    e_moved = False
                    new_state_up = [floor.copy() for floor in old_state]
                    new_state_down = [floor.copy() for floor in old_state]
                    for item_on_floor in items_on_floor:
                        if item_on_floor in cur_pair:
                            if new_state_up is not None:
                                if "E" in old_state[floor_index] and not e_moved:
                                    e_moved = True
                                    if floor_index < len(old_state) - 1:
                                        new_state_up[floor_index].remove("E")
                                        new_state_up[floor_index + 1].append("E")
                                    if floor_index > 0:
                                        new_state_down[floor_index].remove("E")
                                        new_state_down[floor_index - 1].append("E")

                                if floor_index < len(old_state) - 1:
                                    new_state_up[floor_index].remove(item_on_floor)
                                    new_state_up[floor_index + 1].append(item_on_floor)
                                else:
                                    new_state_up = None

                            if new_state_down is not None:
                                if floor_index > 0:
                                    new_state_down[floor_index].remove(item_on_floor)
                                    new_state_down[floor_index - 1].append(item_on_floor)
                                else:
                                    new_state_down = None

                    if is_valid_state(new_state_up):
                        for i in range(len(new_state_up)):
                            new_state_up[i].sort()
                        if str(new_state_up) not in visited_states:
                            next_states.append((cur_pair, new_state_up))
                            network_graph.add_edge(str(old_state), str(new_state_up))

                    if is_valid_state(new_state_down):
                        for i in range(len(new_state_down)):
                            new_state_down[i].sort()
                        if str(new_state_down) not in visited_states:
                            next_states.append((cur_pair, new_state_down))
                            network_graph.add_edge(str(old_state), str(new_state_down))

        # for state in next_states:
        #    print_floors(state[1], state[0])

    states_to_visit = [ns[1] for ns in next_states]

final_state = [[], [], [], all_items + ["E"]]
for i in range(len(final_state)):
    final_state[i].sort()

for i in range(len(initial_state)):
    initial_state[i].sort()

print(nx.dijkstra_path(network_graph, str(initial_state), str(final_state)))
part1 = nx.dijkstra_path_length(network_graph, str(initial_state), str(final_state))
print("Part 1 = " + str(part1))
