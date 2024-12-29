with open("test_input11.txt") as f:
    content = f.readlines()

part1 = 0
monkey_items = {}
monkey_ops = {}
monkey_test_div = {}
monkey_true_throw = {}
monkey_false_throw = {}

monkey_num = None
for cur_line in content:
    cur_line_split = cur_line.strip().split(' ')
    if cur_line_split[0] == "Monkey":
        monkey_num = int(cur_line_split[1][:-1])

    if cur_line_split[0] == "Starting":
        monkey_items[monkey_num] = cur_line.split(":")[1].split(",")
        monkey_items[monkey_num] = [int(item) for item in monkey_items[monkey_num]]

    if cur_line_split[0] == "Operation:":
        monkey_ops[monkey_num] = cur_line.strip().split(":")[1].lstrip()

    if cur_line_split[0] == "Test:":
        monkey_test_div[monkey_num] = int(cur_line_split[-1])

    if len(cur_line_split) > 1 and cur_line_split[1] == "true:":
        monkey_true_throw[monkey_num] = int(cur_line_split[-1])

    if len(cur_line_split) > 1 and cur_line_split[1] == "false:":
        monkey_false_throw[monkey_num] = int(cur_line_split[-1])

monkey_inspection_count = []
for i in range(len(monkey_items)):
    monkey_inspection_count.append(0)

for cur_round in range(1, 10001):
    print("round number " + str(cur_round))
    for monkey_num in range(len(monkey_items)):
        for item in monkey_items[monkey_num]:
            monkey_inspection_count[monkey_num] += 1
            new = 0
            old = item
            exec(monkey_ops[monkey_num])
            test_result = new % monkey_test_div[monkey_num] == 0
            if test_result:
                monkey_items[monkey_true_throw[monkey_num]].append(new)
            else:
                monkey_items[monkey_false_throw[monkey_num]].append(new)
        monkey_items[monkey_num] = []

monkey_inspection_count = list(monkey_inspection_count)
monkey_inspection_count.sort()
part1 = monkey_inspection_count[-1] * monkey_inspection_count[-2]
print("part1 = " + str(part1))
