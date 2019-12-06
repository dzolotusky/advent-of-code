with open("input6.txt") as f:
    content = f.readlines()

orbiting_count = {}

for line in content:
    line = line.strip()
    orbited = line.split(")")[0]
    orbiting = line.split(")")[1]

    orbiting_count[orbiting] = orbited


def count_orbits(orbiting_map, obj):
    if orbiting_map[obj] in orbiting_map:
        return 1 + count_orbits(orbiting_map, orbiting_map[obj])
    else:
        return 1


part1 = 0
for key in orbiting_count.keys():
    part1 += count_orbits(orbiting_count, key)

print(part1)
