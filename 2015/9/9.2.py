with open("input9.txt") as f:
    content = f.readlines()

cities = []
paths = []

for cur_line in content:
    cur_line_split = cur_line.split('=')
    distance = int(cur_line_split[1])
    route = cur_line_split[0].split(' ')
    start_city = route[0].strip()
    end_city = route[2].strip()
    paths.append((start_city, end_city, distance))
    paths.append((end_city, start_city, distance))
    if start_city not in cities:
        cities.append(start_city)
    if end_city not in cities:
        cities.append(end_city)

best_distance = None
best_path = None

for start_city in cities:
    total_distance = 0
    full_path = []
    remaining_cities = cities.copy()
    remaining_cities.remove(start_city)
    cur_city = start_city
    full_path = [cur_city]
    while len(remaining_cities) > 0:
        nearest_distance = None
        nearest_city = None

        for path in paths:
            if path[0] == cur_city:
                if (nearest_distance is None or path[2] > nearest_distance) and path[1] in remaining_cities:
                    nearest_distance = path[2]
                    nearest_city = path[1]
        full_path.append(nearest_city)
        total_distance = total_distance + nearest_distance
        remaining_cities.remove(nearest_city)
        cur_city = nearest_city

    print(full_path)
    print(total_distance)
    if best_distance is None or best_distance < total_distance:
        best_distance = total_distance
        best_path = full_path

print("DONE, BEST:")
print (best_path)
print (best_distance)