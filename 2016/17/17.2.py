import hashlib
from collections import deque

# input = "hijkl"
# input = "ihgpwlah"
# input = "kglvqrro"
# input = "ulqzkmiv"

input = "gdjjyniy"

cur_loc = (0, 0)
goal_loc = (3, 3)

directions = "UDLR"
direction_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_open(door):
    return door in "bcdef"


def convert_to_door_bools(md5hash):
    doors = []
    for cur_char in md5hash[:4]:
        doors.append(is_open(cur_char))

    return doors

paths = []
def shortest_path(loc1, loc2):
    global paths
    if loc1 == loc2:
        return "", 0

    queue = deque([])
    cur_loc = loc1
    queue.append((cur_loc, 0, ""))
    while len(queue) > 0:
        cur_loc, distance, path = queue.popleft()
        if cur_loc == loc2:
            paths.append((path, distance))
        else:
            h = hashlib.md5()
            hash_input = input + path
            h.update(hash_input.encode('utf-8'))
            md5Hash = h.hexdigest()
            for door_index, door_state in enumerate(convert_to_door_bools(md5Hash)):
                if door_state:
                    next_loc = (
                    cur_loc[0] + direction_vectors[door_index][0], cur_loc[1] + direction_vectors[door_index][1])
                    if 0 <= next_loc[0] <= 3 and 0 <= next_loc[1] <= 3:
                        queue.append((next_loc, distance + 1, path + directions[door_index]))

    return None


shortest_path(cur_loc, goal_loc)
paths.sort(key=lambda n: (n[1]), reverse=True)
print(paths[0][1])
