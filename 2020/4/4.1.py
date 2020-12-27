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

part1 = 0
part2 = 0
indx = 0
ids = [""]
for cur_line in content:
    if cur_line == "\n":
        indx += 1
        ids.append("")
    ids[indx] += cur_line

for cur_id in ids:
    valid = True
    for field in required:
        if field not in cur_id:
            valid = False
            break;
    if valid:
        part1 += 1

print("part 1 = " + str(part1))