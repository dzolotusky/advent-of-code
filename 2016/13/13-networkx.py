import networkx as nx

# input = 10
# target = (4, 7)

input = 1364
target = (39, 31)

grid = []
for i in range(0, target[0] + 100):
    sub_array = ['.'] * (target[1] + 100)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        val = j * j + 3 * j + 2 * j * i + i + i * i
        val += input
        ones = bin(val).count('1')
        if ones % 2 == 0:
            grid[i][j] = '.'
        else:
            grid[i][j] = '#'


def print_grid(grid_to_print):
    for i in range(len(grid_to_print)):
        for j in range(len(grid_to_print[i])):
            print(grid_to_print[i][j], end='')
        print('')


network_graph = nx.Graph()
for i in range(len(grid) - 1):
    for j in range(len(grid[i]) - 1):
        if grid[i][j] == '#':
            continue
        if grid[i + 1][j] == '.':
            network_graph.add_edge((i, j), (i + 1, j))
        if grid[i][j + 1] == '.':
            network_graph.add_edge((i, j), (i, j + 1))

# part1 = nx.dijkstra_path(network_graph, (1, 1), target, 'distance')
# print(part1)

part1_time = nx.dijkstra_path_length(network_graph, (1, 1), target, 'distance')
print(part1_time)
