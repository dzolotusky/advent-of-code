with open("input12.txt") as f:
    content = f.readlines()

part2 = 0
paths = {}
small_caves = []

for cur_line in content:
    cur_line_split = cur_line.split("-")
    start = cur_line_split[0].strip()
    end = cur_line_split[1].strip()

    if start not in paths:
        paths[start] = []
    if end not in paths:
        paths[end] = []

    paths[start].append(end)
    paths[end].append(start)

    if start.islower() and start not in ["start", "end"]:
        small_caves.append(start)
    if end.islower() and end not in ["start", "end"]:
        small_caves.append(end)
small_caves = set(small_caves)

all_paths = []
def find_paths(cur_location, cur_path, small_cave_exception):
    if cur_location == "end":
        cur_path.append(cur_location)
        if cur_path not in all_paths:
            all_paths.append(cur_path)
            return 1
        else:
            return 0

    if cur_location.islower() and cur_location in cur_path:
        if cur_location == small_cave_exception:
            if cur_path.count(cur_location) == 2:
                return 0
        else:
            return 0

    cur_path.append(cur_location)
    total = 0

    if cur_location in paths:
        next_steps = paths[cur_location]
        for step in next_steps:
            total += find_paths(step, cur_path.copy(), small_cave_exception)

    return total


for small_cave in small_caves:
    part2 += find_paths("start", [], small_cave)

print("part 2 = " + str(part2))
