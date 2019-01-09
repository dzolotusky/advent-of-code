with open("input16.txt") as f:
    content = f.readlines()

gift_giver = {"children": 3,
              "cats": 7,
              "samoyeds": 2,
              "pomeranians": 3,
              "akitas": 0,
              "vizslas": 0,
              "goldfish": 5,
              "trees": 3,
              "cars": 2,
              "perfumes": 1}

sues = []

for cur_line in content:
    colon_loc = cur_line.index(":")
    sue_num = int(cur_line[3:colon_loc])
    props = cur_line[colon_loc + 1:].strip().split(",")
    sue_props = []
    for prop in props:
        prop_split = prop.split(":")
        prop_name = prop_split[0].rstrip().lstrip()
        prop_val = int(prop_split[1])
        sue_props.append((prop_name, prop_val))
    sues.append((sue_num, sue_props))

for cur_sue in sues:
    found_sue = True

    for cur_prop in cur_sue[1]:
        cur_prop_name = cur_prop[0]
        cur_prop_val = cur_prop[1]

        if cur_prop_name in gift_giver:
            if cur_prop_name in ["cats", "trees"]:
                if cur_prop_val <= gift_giver[cur_prop_name]:
                    found_sue = False
                    break
                continue
            else:
                if cur_prop_name in ["pomeranians", "goldfish"]:
                    if cur_prop_val >= gift_giver[cur_prop_name]:
                        found_sue = False
                        break
                    continue
                else:
                    if cur_prop_val != gift_giver[cur_prop_name]:
                        found_sue = False
                        break
        else:
            found_sue = False
            break

    if found_sue:
        print("Found gift giving Sue, it's " + str(cur_sue[0]))
