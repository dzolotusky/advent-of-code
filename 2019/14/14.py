import math
import networkx as nx

with open("input14.txt") as f:
    content = f.readlines()

replacements = {}
network_graph = nx.DiGraph()

for cur_line in content:
    cur_line_split = cur_line.split("=>")
    initial_val = cur_line_split[0].strip().split(",")
    initial_val = list(map(str.strip, initial_val))
    replaced_val = cur_line_split[1].strip()
    if "," in replaced_val:
        print("multiple products")
        exit(1)

    product = replaced_val.split(" ")[1]
    quantity_of_product = replaced_val.split(" ")[0]

    if product in replacements:
        print("multiple ways to make a product")
        exit(1)

    replacements[product] = [quantity_of_product] + initial_val
    for value in initial_val:
        cur_ingredient = value.split(' ')[1]
        network_graph.add_edge(product, cur_ingredient)


total_needs = {}


def how_to_make(goal, quantity, all_extras):
    if goal == "ORE":
        return all_extras

    if goal in all_extras:
        if all_extras[goal] > quantity:
            all_extras[goal] -= quantity
            return 0, all_extras
        else:
            quantity -= all_extras[goal]
            all_extras[goal] = 0

    needs = replacements[goal]
    multiple = 1
    amount_made = int(needs[0])

    if amount_made < quantity:
        multiple = math.ceil(quantity / amount_made)
        amount_made *= multiple

    if amount_made > quantity:
        extra = amount_made - quantity
        if goal in all_extras:
            all_extras[goal] += extra
        else:
            all_extras[goal] = extra

    for ingredient in needs[1::]:
        ingredient_split = ingredient.split(' ')
        if ingredient_split[1] not in total_needs:
            total_needs[ingredient_split[1]] = 0
        total_needs[ingredient_split[1]] += int(ingredient_split[0]) * multiple
    return all_extras


all_leftover = {}
total_needs["FUEL"] = 1

ordered_list = list(nx.topological_sort(network_graph))

for current_ingredient in ordered_list:
    all_leftover = how_to_make(current_ingredient, total_needs[current_ingredient], all_leftover)

print("Part 1 = " + str(total_needs["ORE"]))

#total_needs["FUEL"] = 3061522 # binary searched to find this value

#for current_ingredient in ordered_list:
#    all_leftover = how_to_make(current_ingredient, total_needs[current_ingredient], all_leftover)

print("Part 2 = " + str(3061522))
