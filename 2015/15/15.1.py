with open("input15.txt") as f:
    content = f.readlines()

ingredients = []

for cur_line in content:
    colon_loc = cur_line.index(":")
    name = cur_line[:colon_loc]
    cur_line_split = cur_line[colon_loc + 2:].strip().split(" ")
    capacity = int(cur_line_split[1][:-1])
    durability = int(cur_line_split[3][:-1])
    flavor = int(cur_line_split[5][:-1])
    texture = int(cur_line_split[7][:-1])
    calories = int(cur_line_split[9])
    ingredients.append((capacity, durability, flavor, texture, calories, name))

print(ingredients)

highest_score = 0


# returns the score of a cookie with the ingredient combo specified in the passed in list
def cookie_score(cookie_contents):
    total_ingredients = [0] * 4
    for ind, count in enumerate(cookie_contents):
        for ingredient in range(4):
            total_ingredients[ingredient] = total_ingredients[ingredient] + count * ingredients[ind][ingredient]

    score = 1
    for ing_score in total_ingredients:
        if ing_score < 0:
            return 0
        score = score * ing_score

    return score


# print(cookie_score([44, 56])) # verify that cookie_score matches example

highest_score = -1
best_combo = None


def find_highest_score(cur_values):
    global highest_score
    global best_combo
    cur_total = max(0, sum(cur_values))
    first_missing = None
    for i, cur_val in enumerate(cur_values):
        if cur_val == -1:
            first_missing = i
            break

    if first_missing == None:
        score = cookie_score(cur_values)
        if score > highest_score:
            highest_score = score
            best_combo = cur_values
    else:
        for option in range(0, 100 - cur_total):
            cur_values[first_missing] = option
            find_highest_score(cur_values.copy())


find_highest_score([-1] * len(ingredients))

print(highest_score)
print(best_combo)
