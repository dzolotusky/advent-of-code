with open("input7.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 0
inner_to_outer = {}
outer_to_inner = {}

for cur_line in content:
    cur_line_split = cur_line.split("contain")
    outer = cur_line_split[0][0:cur_line_split[0].strip().rfind(" ")]
    inner_split = cur_line_split[1].split(",")
    outer_to_inner[outer] = {}
    for inner_bag in inner_split:
        inner_bag = inner_bag.lstrip()
        bag_color = inner_bag[1 + inner_bag.find(" "):(1 + inner_bag.strip().rfind(" "))]
        bag_color = bag_color.strip()
        if bag_color != "other":
            if bag_color in inner_to_outer:
                inner_to_outer[bag_color].append(outer)
            else:
                inner_to_outer[bag_color] = [outer]
            outer_to_inner[outer][bag_color] = int(inner_bag[:1 + inner_bag.find(" ")])

my_bag = "shiny gold"
new_options_for_outer = set(inner_to_outer[my_bag])
options_for_outer = set()
while new_options_for_outer != options_for_outer:
    added = False
    options_for_outer = new_options_for_outer.copy()
    for option in options_for_outer:
        if option in inner_to_outer:
            for outer_option in inner_to_outer[option]:
                new_options_for_outer.add(outer_option)

part1 = len(new_options_for_outer)

my_bags = {my_bag: 1}
new_bags = outer_to_inner[my_bag]
my_bags = my_bags | new_bags
while len(new_bags) > 0:
    added_bags = {}
    for bag in new_bags:
        inner_bags = outer_to_inner[bag]
        for inner_bag in inner_bags:
            if inner_bag in my_bags:
                my_bags[inner_bag] += inner_bags[inner_bag] * new_bags[bag]
            else:
                my_bags[inner_bag] = inner_bags[inner_bag] * new_bags[bag]

            if inner_bag in added_bags:
                added_bags[inner_bag] += inner_bags[inner_bag] * new_bags[bag]
            else:
                added_bags[inner_bag] = inner_bags[inner_bag] * new_bags[bag]

    new_bags = added_bags



print(my_bags)
for bag_color in my_bags:
    part2 += my_bags[bag_color]

print("part 1 = " + str(part1))
print("part 2 = " + str(part2 - 1))