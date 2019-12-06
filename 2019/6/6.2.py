with open("input6.txt") as f:
    content = f.readlines()

orbiting_count = {}

for line in content:
    line = line.strip()
    orbited = line.split(")")[0]
    orbiting = line.split(")")[1]

    orbiting_count[orbiting] = orbited

visited = []


def count_transfers(orbiting_map, obj, counter):
    visited.append(obj)
    if obj == "SAN":
        print("done " + str(counter - 2))
        exit()
    options = []
    if orbiting_map[obj] in orbiting_map:
        if orbiting_map[obj] not in visited:
            options.append(orbiting_map[obj])
    for key in orbiting_map.keys():
        if orbiting_map[key] == obj:
            if key not in visited:
                options.append(key)

    if len(options) == 2:
        count_transfers(orbiting_map, options[0], 1 + counter)
        count_transfers(orbiting_map, options[1], 1 + counter)
    else:
        if len(options) == 1:
            count_transfers(orbiting_map, options[0], 1 + counter)

count_transfers(orbiting_count, "YOU", 0)