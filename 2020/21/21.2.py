with open("input21.txt") as f:
    content = f.readlines()

part1 = 0
all_allergens = []
all_ingredients = []
foods = []
for cur_line in content:
    cur_line = cur_line[:-2]
    ingredients = cur_line[:cur_line.find("(")].split()
    allergens = cur_line[cur_line.find("contains ") + len("contains "):].split(", ")
    all_allergens = all_allergens + allergens
    all_ingredients = all_ingredients + ingredients
    foods.append((ingredients, allergens))

all_allergens = set(all_allergens)
all_ingredients = set(all_ingredients)
allergic_ingredients = {}

# narrow down potential allergic ingredients to intersection of foods that have the allergen
for cur_allergen in all_allergens:
    potential_allergic_ingredients = []
    for cur_food in foods:
        if cur_allergen in cur_food[1]:
            if len(potential_allergic_ingredients) == 0:
                potential_allergic_ingredients = cur_food[0]
            else:
                potential_allergic_ingredients = list(set(potential_allergic_ingredients) & set(cur_food[0]))

    allergic_ingredients[cur_allergen] = potential_allergic_ingredients

non_allergic = all_ingredients
for allergic_ingredient in allergic_ingredients:
    non_allergic = non_allergic - set(allergic_ingredients[allergic_ingredient])

for cur_food in foods:
    for cur_ingredient in cur_food[0]:
        if cur_ingredient in non_allergic:
            part1 += 1

print("part 1 = " + str(part1))


def max_len(items):
    max_length = 0
    for cur_item in items:
        cur_length = len(items[cur_item])
        if cur_length > max_length:
            max_length = cur_length

    return max_length


while max_len(allergic_ingredients) > 1:
    visited = []
    for cur_allergic_ingredient in allergic_ingredients:
        if len(allergic_ingredients[cur_allergic_ingredient]) == 1 and cur_allergic_ingredient not in visited:
            for second_allergic_ingredient in allergic_ingredients:
                if second_allergic_ingredient == cur_allergic_ingredient:
                    continue
                if allergic_ingredients[cur_allergic_ingredient][0] in allergic_ingredients[second_allergic_ingredient]:
                    allergic_ingredients[second_allergic_ingredient].remove(allergic_ingredients[cur_allergic_ingredient][0])
                visited.append(cur_allergic_ingredient)

all_allergens = list(all_allergens)
all_allergens.sort()

part2 = []
for cur_allergen in all_allergens:
    part2.append(allergic_ingredients[cur_allergen][0])
part2 = ",".join(part2)
print(part2)