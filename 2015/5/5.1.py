with open("input5.txt") as f:
    content = f.readlines()

nice_count = 0
naughty_count = 0

for cur_line in content:
    vowel_count = 0
    match = False
    naughty = False
    for indx, cur_char in enumerate(cur_line):
        #    print(cur_line[indx:indx+1])
        if indx < len(cur_line) - 1 and cur_line[indx:indx + 2] in ["ab", "cd", "pq", "xy"]:
            naughty = True
            break

        if cur_char in "aeiou":
            vowel_count = vowel_count + 1

        if indx < len(cur_line) - 1 and cur_char == cur_line[indx + 1]:
            match = True

    if match and vowel_count > 2 and not naughty:
        nice_count = nice_count + 1
    else:
        naughty_count = naughty_count + 1

#  print(naughty)
#  print(match)
#  print(vowel_count)

print("nice = " + str(nice_count))
print("naughty = " + str(naughty_count))
