with open("input5.txt") as f:
    content = f.readlines()

nice_count = 0
naughty_count = 0

for cur_line in content:
    rule1 = False
    rule2 = False

    for indx, cur_char in enumerate(cur_line):
        if indx < len(cur_line) - 2 and cur_char == cur_line[indx + 2]:
            rule2 = True

        if cur_line[indx:indx + 2] in cur_line[indx + 2:]:
            rule1 = True

    if rule1 and rule2:
        nice_count = nice_count + 1
    else:
        naughty_count = naughty_count + 1

#  print(rule1)
#  print(rule2)

print("nice = " + str(nice_count))
print("naughty = " + str(naughty_count))
