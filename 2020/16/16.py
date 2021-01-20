with open("input16.txt") as f:
    content = f.readlines()

part1 = 0
part2 = 1
fields = {}
my_ticket = []
tickets = []


def list_to_int(str_list):
    return [int(num) for num in str_list]


for line_no in range(len(content)):
    field = content[line_no]
    if field == "\n":
        break

    field_split = field.split(": ")
    field_name = field_split[0]
    range_strs = field_split[1].split(" or ")
    ranges = [str.strip().split("-") for str in range_strs]
    ranges = [list_to_int(r) for r in ranges]
    fields[field_name] = ranges

line_no += 2

my_ticket = [int(num) for num in content[line_no].strip().split(",")]

line_no += 3
while line_no < len(content):
    tickets.append([int(num) for num in content[line_no].strip().split(",")])
    line_no += 1

invalid_tickets = []
for cur_indx in range(len(tickets)):
    cur_ticket = tickets[cur_indx]
    for value in cur_ticket:
        valid = False
        for ranges in fields.values():
            for cur_range in ranges:
                if cur_range[0] <= value <= cur_range[1]:
                    valid = True
        if not valid:
            part1 += value
            invalid_tickets.append(cur_indx)

for indx in reversed(invalid_tickets):
    del tickets[indx]

not_field_indexes = {}
for field_indx in range(len(fields)):
    not_field_indexes[field_indx] = []
for cur_indx in range(len(tickets)):
    cur_ticket = tickets[cur_indx]
    for value_indx in range(len(cur_ticket)):
        value = cur_ticket[value_indx]
        for field_indx in range(len(fields.values())):
            ranges = list(fields.values())[field_indx]
            if not ranges[0][0] <= value <= ranges[0][1] and not ranges[1][0] <= value <= ranges[1][1]:
                not_field_indexes[field_indx].append(value_indx)

field_mappings = {}
while len(field_mappings) < len(fields):
    for exclusions in not_field_indexes:
        if len(not_field_indexes[exclusions]) == len(fields) - len(field_mappings) - 1:
            for field_num in range(len(fields) + 1):
                if field_num not in not_field_indexes[exclusions] and field_num not in field_mappings.values():
                    field_mappings[exclusions] = field_num

field_index = 0
for field in fields:
    if field.startswith("departure"):
        part2 *= my_ticket[field_mappings[field_index]]
    field_index += 1

print("part 1 = " + str(part1))
print("part 2 = " + str(part2))