import networkx as nx

with open("input15.txt") as f:
    content = f.readlines()

part1 = 0
grid = []
network_graph = nx.DiGraph()


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


for i in range(len(content) * 5):
    sub_array = ['.'] * ((len(content[0]) - 1) * 5)
    grid.append(sub_array)

for i in range(len(content)):
    for j in range(len(content)):
        grid[i][j] = int(content[i][j])
        for copy in range(1, 5):
            grid[i + copy * len(content)][j] = (int(content[i][j]) + copy)
            if grid[i + copy * len(content)][j] > 9:
                grid[i + copy * len(content)][j] -= 9

for i in range(len(grid)):
    for j in range(len(content)):
        for copy in range(1, 5):
            grid[i][j + copy * len(content)] = (int(grid[i][j]) + copy)
            if grid[i][j + copy * len(content)] > 9:
                grid[i][j + copy * len(content)] -= 9

goal = (len(grid) - 1, len(grid[len(grid[:-1])]) - 1)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i - 1 >= 0:
            network_graph.add_edge((i, j), (i - 1, j), weight=grid[i - 1][j])
        if i + 1 < len(grid):
            network_graph.add_edge((i, j), (i + 1, j), weight=grid[i + 1][j])
        if j - 1 >= 0:
            network_graph.add_edge((i, j), (i, j - 1), weight=grid[i][j - 1])
        if j + 1 < len(grid[i]):
            network_graph.add_edge((i, j), (i, j + 1), weight=grid[i][j + 1])

part1 = nx.dijkstra_path_length(network_graph, (0, 0), goal)
print("part 1 = " + str(part1))
