import networkx as nx

with open("input15.txt") as f:
    content = f.readlines()

part1 = 0
grid = []
goal = (len(content) - 1, len(content[len(content[:-1])]) - 1)
network_graph = nx.DiGraph()

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = int(content[i][j])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i + 1 < len(grid):
            network_graph.add_edge((i, j), (i + 1, j), weight=grid[i + 1][j])
        if j + 1 < len(grid[i]):
            network_graph.add_edge((i, j), (i, j + 1), weight=grid[i][j + 1])

part1 = nx.dijkstra_path_length(network_graph, (0, 0), goal)
print("part 1 = " + str(part1))
