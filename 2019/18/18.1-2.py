from collections import deque

with open("test_input18.txt") as f:
    content = f.readlines()

grid = []
start = (None, None)
all_keys = set([])

for i in range(len(content)):
    sub_array = ['.'] * (len(content[0]) - 1)
    grid.append(sub_array)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = content[i][j]
        if ord('z') >= ord(content[i][j]) >= ord('a'):
            all_keys.add(content[i][j])

        if content[i][j] == '@':
            start = (i, j)
            grid[i][j] = '.'


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()


min_dist = None


def can_go(pos, keys):
    if ord('z') >= ord(grid[pos[0]][pos[1]]) >= ord('a'):
        return True

    if ord('Z') >= ord(grid[pos[0]][pos[1]]) >= ord('A'):
        if grid[pos[0]][pos[1]].lower() in keys:
            return True

    return False


def walk(pos, cur_dist, keys, visited):
    queue = deque([])
    #grid[pos[0]][pos[1]] = cur_dist % 10
    global min_dist

    queue.append((pos, -1, set([]), []))
    while len(queue) > 0:
        pos, cur_dist, keys, visited = queue.popleft()
        if (pos, keys) not in visited:
            visited.append((pos, keys))

            if ord('z') >= ord(grid[pos[0]][pos[1]]) >= ord('a'):
                if grid[pos[0]][pos[1]] not in keys:
                    keys.add(grid[pos[0]][pos[1]])

            cur_dist += 1
            #print(str(cur_dist) + " : " + str(pos))
            if len(keys) == len(all_keys):
                print(cur_dist)
                if (min_dist is None or cur_dist < min_dist):
                    min_dist = cur_dist
                return

            if grid[pos[0] + 1][pos[1]] == '.' or can_go((pos[0] + 1, pos[1]), keys):
                queue.append(((pos[0] + 1, pos[1]), cur_dist, keys.copy(), visited.copy()))
            if grid[pos[0] - 1][pos[1]] == '.' or can_go((pos[0] - 1, pos[1]), keys):
                queue.append(((pos[0] - 1, pos[1]), cur_dist, keys.copy(), visited.copy()))
            if grid[pos[0]][pos[1] + 1] == '.' or can_go((pos[0], pos[1] + 1), keys):
                queue.append(((pos[0], pos[1] + 1), cur_dist, keys.copy(), visited.copy()))
            if grid[pos[0]][pos[1] - 1] == '.' or can_go((pos[0], pos[1] - 1), keys):
                queue.append(((pos[0], pos[1] - 1), cur_dist, keys.copy(), visited.copy()))


walk(start, -1, set([]), [])
#print_grid()
print(str(min_dist))
