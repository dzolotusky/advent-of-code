import networkx

with open("test_input19.txt") as f:
    content = f.readlines()

part1 = 0
beacons = []
for cur_line in content:
    if "scanner" in cur_line:
        cur_line_split = cur_line.split()
        scanner_num = int(cur_line_split[2])
        beacons.append([])
    else:
        if len(cur_line) > 1:
            point = [int(s) for s in cur_line.strip().split(",")]
            beacons[scanner_num].append(tuple(point))

deltas = []
for scanner_index, scanner in enumerate(beacons):
    deltas.append([])
    for outer_index, outer_beacon in enumerate(scanner):
        for inner_index, inner_beacon in enumerate(scanner):
            if inner_index <= outer_index:
                continue
            delta = [outer_beacon[0] - inner_beacon[0], outer_beacon[1] - inner_beacon[1],
                     outer_beacon[2] - inner_beacon[2]]
            deltas[scanner_index].append((delta, (outer_index, inner_index)))

scanner_overlap = {}
for outer_scanner_index, outer_scanner in enumerate(deltas):
    for inner_scanner_index, inner_scanner in enumerate(deltas):
        if inner_scanner_index == outer_scanner_index:
            continue
        counter = 0
        overlap = []
        potential_mappings = {}
        for outer_delta_index, outer_delta in enumerate(outer_scanner):
            for inner_delta_index, inner_delta in enumerate(inner_scanner):
                matches = 0
                inner_ignore = []
                cur_mapping = [0] * 3
                for outer_coord_index, outer_coord in enumerate(outer_delta[0]):
                    for inner_coord_index, inner_coord in enumerate(inner_delta[0]):
                        if inner_coord_index in inner_ignore:
                            continue
                        if abs(outer_coord) == abs(inner_coord):
                            cur_mapping[outer_coord_index] = inner_coord_index + 1
                            if outer_coord > 0 > inner_coord or outer_coord < 0 < inner_coord:
                                cur_mapping[outer_coord_index] *= -1
                            matches += 1
                            inner_ignore.append(inner_coord_index)

                if matches >= 3:
                    counter += 1
                    overlap.append((outer_delta[1], inner_delta[1]))
                    if matches > 3:
                        print((outer_delta, inner_delta, matches))

                    if 0 not in cur_mapping:
                        cur_mapping = tuple(cur_mapping)
                        if cur_mapping not in potential_mappings:
                            potential_mappings[cur_mapping] = 1
                        else:
                            potential_mappings[cur_mapping] += 1

        if counter >= 66:  # 12 overlaps
            mapping = [0] * 3
            max_mapping = 0
            for pot_map in potential_mappings:
                if potential_mappings[pot_map] > max_mapping:
                    mapping = pot_map
                    max_mapping = potential_mappings[pot_map]
            scanner_overlap[outer_scanner_index, inner_scanner_index] = (overlap, mapping)
            #break

# print(scanner_overlap)
scanner_overlap_beacons = {}
for scn_ovr in scanner_overlap:
    overlap_records = scanner_overlap[scn_ovr][0]
    beacon_indexes = {}
    for overlap_pair in overlap_records:
        potential_matches = [overlap_pair[1][0], overlap_pair[1][1]]
        for delta_index in overlap_pair[0]:
            if delta_index in beacon_indexes:
                if isinstance(beacon_indexes[delta_index], list):
                    if potential_matches[0] in beacon_indexes[delta_index] and potential_matches[1] not in \
                            beacon_indexes[delta_index]:
                        beacon_indexes[delta_index] = (potential_matches[0], scanner_overlap[scn_ovr][1])
                    else:
                        if potential_matches[1] in beacon_indexes[delta_index] and potential_matches[0] not in \
                                beacon_indexes[delta_index]:
                            beacon_indexes[delta_index] = (potential_matches[1], scanner_overlap[scn_ovr][1])
            else:
                beacon_indexes[delta_index] = potential_matches
    scanner_overlap_beacons[scn_ovr] = beacon_indexes

# print(scanner_overlap_beacons)
# print("from scanner 0")
# for first_overlap_beacon in scanner_overlap_beacons[(0,1)]:
#    print((beacons[0][first_overlap_beacon], scanner_overlap_beacons[(0,1)][first_overlap_beacon][1]))

# print("from scanner 1")
# for first_overlap_beacon in scanner_overlap_beacons[(0,1)]:
#    print(beacons[1][scanner_overlap_beacons[(0,1)][first_overlap_beacon][0]])

first_overlap_beacon = list(scanner_overlap_beacons[(0, 1)].keys())[0]


def map_beacon(s_orig, s_dest, sorig_loc, scanner_loc):
    overlap = scanner_overlap_beacons[(s_dest, s_orig)]
    mapping = overlap[list(overlap.keys())[0]][1]
    mapped_dest_coord = [0] * 3
    for coord_index in range(3):
        mapped_dest_coord[coord_index] = sorig_loc[abs(mapping[coord_index]) - 1]
        if mapping[coord_index] < 0:
            mapped_dest_coord[coord_index] *= -1
            #mapped_dest_coord[abs(mapping[coord_index]) - 1] *= -1 #dzolo:unsure about this one
        mapped_dest_coord[coord_index] += scanner_loc[coord_index]

    return mapped_dest_coord


def map_scanner(s_orig, s_dest, orig_beacon, dest_beacon):
    overlap = scanner_overlap_beacons[(s_dest, s_orig)]
    mapping = overlap[list(overlap.keys())[0]][1]
    print(mapping)
    mapped_dest_coord = [0] * 3
    for coord_index in range(3):
        mapped_dest_coord[coord_index] = orig_beacon[abs(mapping[coord_index]) - 1]
        #mapped_dest_coord[abs(mapping[coord_index]) - 1] = orig_beacon[coord_index]

    for coord_index in range(3):
        if mapping[coord_index] < 0:
#            mapped_dest_coord[coord_index] *= -1
            mapped_dest_coord[abs(mapping[coord_index]) - 1] *= -1

#    dest_scanner_loc = [None, None, None]
#    dest_scanner_loc[abs(mapping[0]) - 1] = dest_beacon[abs(mapping[0]) - 1] - mapped_dest_coord[0]
#    dest_scanner_loc[abs(mapping[1]) - 1] = dest_beacon[abs(mapping[1]) - 1] - mapped_dest_coord[1]
#    dest_scanner_loc[abs(mapping[2]) - 1] = dest_beacon[abs(mapping[2]) - 1] - mapped_dest_coord[2]
    dest_scanner_loc = (dest_beacon[0] - mapped_dest_coord[0],
                        dest_beacon[1] - mapped_dest_coord[1],
                        dest_beacon[2] - mapped_dest_coord[2])

    return dest_scanner_loc


#s0_beacon = beacons[0][first_overlap_beacon]
#s1_beacon = beacons[1][scanner_overlap_beacons[(0, 1)][first_overlap_beacon][0]]

#print("test")
#s1_scanner_loc_in_s0 = map_scanner(1, 0, s1_beacon, s0_beacon)
#print("s1 from s0: " + str(s1_scanner_loc_in_s0))
#print("s1.b1 from s0 " + str(beacons[1][0]) + " -> " + str(map_beacon(1, 0, beacons[1][0], s1_scanner_loc_in_s0)))

all_beacons_from_s0 = beacons[0]

graph_of_mappings = networkx.DiGraph()
for mapping in scanner_overlap_beacons:
    graph_of_mappings.add_edge(mapping[0], mapping[1])

count_of_duplicate_beacons = 0
for scanner_index in range(1, len(beacons)):
    path = networkx.shortest_path(graph_of_mappings, scanner_index, 0)
    print(path)
    origin = scanner_index
    cur_beacon_locs = beacons[origin].copy()
    dest_scanner_loc = None
    original_scanner_mapped = [0,0,0]
    for dest in path[1:]:
        dest_beacon_locs = []
        dest_beacon_index = list(scanner_overlap_beacons[(dest, origin)].keys())[0]
        dest_beacon = beacons[dest][dest_beacon_index]
        origin_beacon_index = scanner_overlap_beacons[(dest, origin)][dest_beacon_index][0]
        origin_beacon = beacons[origin][origin_beacon_index]
        dest_scanner_loc = map_scanner(origin, dest, origin_beacon, dest_beacon)
        for cur_beacon_index in range(len(cur_beacon_locs)):
            dest_beacon_loc = map_beacon(origin, dest, cur_beacon_locs[cur_beacon_index], dest_scanner_loc)
            dest_beacon_locs.append(dest_beacon_loc)
        original_scanner_mapped = map_beacon(origin, dest, original_scanner_mapped, dest_scanner_loc)
        cur_beacon_locs = dest_beacon_locs
        origin = dest

    print("scanner loc for " + str(scanner_index) + " : " + str(original_scanner_mapped))
    for beacon_loc in cur_beacon_locs:
        s0_beacon_loc_tup = tuple(beacon_loc)
        if s0_beacon_loc_tup in all_beacons_from_s0:
            count_of_duplicate_beacons += 1
        else:
            all_beacons_from_s0.append(s0_beacon_loc_tup)



# s1_scanner_loc_in_s0 = None
# count = 0
# for s1_beacon_index in range(len(beacons[1])):
#     for cur_s0_beacon in scanner_overlap_beacons[(0, 1)]:
#         if scanner_overlap_beacons[(0, 1)][cur_s0_beacon][0] == s1_beacon_index:
#             s0_beacon = beacons[0][cur_s0_beacon]
#     s1_beacon = beacons[1][s1_beacon_index]
#     if s1_scanner_loc_in_s0 is None:
#         s1_scanner_loc_in_s0 = map_scanner(1, 0, s1_beacon, s0_beacon)
#     s1_beacon_in_s0 = tuple(map_beacon(1, 0, s1_beacon, s1_scanner_loc_in_s0))
#     if s1_beacon_in_s0 in all_beacons_from_s0:
#         count += 1
#     else:
#         all_beacons_from_s0.append(s1_beacon_in_s0)

# print("duplicates: " + str(count_of_duplicate_beacons))
# print("---all beacons from s0--- (" + str(len(all_beacons_from_s0)) + str(")"))
# for beacon in all_beacons_from_s0:
#     for coord_index, coord in enumerate(beacon):
#         print(coord, end='')
#         if coord_index < 2:
#             print(",", end='')
#     print()

print("matches = " + str(counter))
print("part 1 = " + str(part1))
