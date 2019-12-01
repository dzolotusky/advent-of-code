#input = 300
input = 3001330

elves = {}

for i in range(input):
    elves[i] = 1


def play_round():
    ind = 0
    while ind < len(elves):
        keys = list(elves.keys())
        next_key = (keys.index(keys[ind]) + 1) % len(keys)
        elves[keys[ind]] += elves[keys[next_key]]
        elves.pop(keys[next_key])
        ind += 1

counter = 0
start = 1
target_len = input
while (target_len > 1):
    #play_round()
    #remaining = [val + 1 for val in list(elves.keys())]
    #print(str(len(remaining)) + ":" + str(remaining))
    counter += 1

    if target_len > 1 and target_len % 2 != 0:
        start += (2 ** counter)
    target_len = int(input / (2 ** counter))
#    print(str(target_len) + ":" + str(2 ** counter)+ ":" + str(start))


print("Part 1 = " + str(start))

#any iteration = len = input / iteration num