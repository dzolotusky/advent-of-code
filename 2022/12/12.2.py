import math

import networkx as nx

with open("input12.txt") as f:
    content = f.readlines()

grid = []
S_list = []
S = None
E = None

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = ord(content[i][j])
        if content[i][j] == "a":
            S_list.append((i, j, ord("a")))
        if content[i][j] == "S":
            S = (i, j, ord("S"))
        if content[i][j] == "E":
            E = (i, j, ord("z"))
            grid[i][j] = ord("z")


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()


network_graph = nx.DiGraph()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i + 1 < len(grid):
            if grid[i + 1][j] - grid[i][j] < 2 or grid[i][j] == ord("S") or grid[i + 1][j] == ord("E"):
                network_graph.add_edge((i, j, grid[i][j]), (i + 1, j, grid[i + 1][j]))
        if j + 1 < len(grid[i]):
            if grid[i][j + 1] - grid[i][j] < 2 or grid[i][j] == ord("S") or grid[i][j + 1] == ord("E"):
                network_graph.add_edge((i, j, grid[i][j]), (i, j + 1, grid[i][j + 1]))
        if i - 1 >= 0:
            if grid[i-1][j] - grid[i][j] < 2 or grid[i][j] == ord("S") or grid[i - 1][j] == ord("E"):
                network_graph.add_edge((i, j, grid[i][j]), (i - 1, j, grid[i - 1][j]))
        if j - 1 >= 0:
            if grid[i][j-1] - grid[i][j] < 2 or grid[i][j] == ord("S") or grid[i][j - 1] == ord("E"):
                network_graph.add_edge((i, j, grid[i][j]), (i, j - 1, grid[i][j - 1]))

part2 = math.inf
for cur_s in S_list:
    try:
        cur_length = nx.dijkstra_path_length(network_graph, cur_s, E)

    except:
        continue
    if cur_length < part2:
        part2 = cur_length
print("part2 = " + str(part2))
