with open("input12.txt") as f:
    content = f.readlines()

part1 = 0
paths = {}

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


def find_paths(cur_location, cur_path):
    if cur_location == "end":
        cur_path.append(cur_location)
        return 1

    if cur_location.islower() and cur_location in cur_path:
        return 0

    cur_path.append(cur_location)
    total = 0

    if cur_location in paths:
        next_steps = paths[cur_location]
        for step in next_steps:
            total += find_paths(step, cur_path.copy())

    return total


part1 = find_paths("start", [])

print("part 1 = " + str(part1))
