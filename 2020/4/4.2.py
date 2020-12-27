import re

with open("input4.txt") as f:
    content = f.readlines()

required = ["byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid"]
            #"cid"]

part2 = 0
indx = 0
ids = [""]
for cur_line in content:
    if cur_line == "\n":
        indx += 1
        ids.append("")
    ids[indx] += cur_line.strip() + " "

ids_map = []
for cur_id in ids:
    cur_id = cur_id.strip().split(" ")
    cur_id_map = {}
    for entry in cur_id:
        keyval = entry.split(":")
        cur_id_map[keyval[0]] = keyval[1]
    ids_map.append(cur_id_map)

for cur_id_map in ids_map:
    valid = True
    for field in required:
        if field not in cur_id_map.keys():
            valid = False
            break
        try:
            if field == "byr":
                byr_val = int(cur_id_map["byr"])
                if byr_val < 1920 or byr_val > 2002:
                    valid = False
                    break
            if field == "iyr":
                byr_val = int(cur_id_map["iyr"])
                if byr_val < 2010 or byr_val > 2020:
                    valid = False
                    break
            if field == "eyr":
                eyr_val = int(cur_id_map["eyr"])
                if eyr_val < 2020 or eyr_val > 2030:
                    valid = False
                    break
            if field == "pid":
                pid_val = int(cur_id_map["pid"])
                if pid_val < 0 or pid_val > 1000000000 or len(cur_id_map["pid"]) < 9:
                    valid = False
                    break
            if field == "ecl":
                if cur_id_map["ecl"] not in ["amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth"]:
                    valid = False
                    break
            if field == "hcl":
                hcl_val = cur_id_map["hcl"]
                hcl_len = len(hcl_val)
                pattern = re.compile("[a-z0-9]+")
                if not pattern.fullmatch(hcl_val[1:]) or hcl_len != 7 or hcl_val[0] != "#":
                    valid = False
                    break
            if field == "hgt":
                hgt_val = cur_id_map["hgt"]
                hgt_char = hgt_val[-2:]
                if hgt_char != "in" and hgt_char != "cm":
                    valid = False
                    break
                else:
                    hgt_num = int(hgt_val[:-2])
                    if hgt_char == "in" and (hgt_num < 59 or hgt_num > 76):
                        valid = False
                        break
                    else:
                        if hgt_char == "cm" and (hgt_num < 150 or hgt_num > 193):
                            valid = False
                            break
        except (ValueError, TypeError):
            valid = False
            break
    if valid:
        part2 += 1

print("part 2 = " + str(part2))