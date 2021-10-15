with open("input19.2.txt") as f:
    content = f.readlines()

part2 = 0
parsed_rules = {}
line_num = 0

for cur_line in content:
    line_num += 1
    if ":" in cur_line:
        rule_num = int(cur_line.split(":")[0])
        rules_data = cur_line.split(":")[1].split("|")
        for rule_data in rules_data:
            subrule_nums = [sub_str for sub_str in rule_data.lstrip().strip().split(" ")]
            subrule_nums = [int(sub_str) if sub_str.isdigit() else sub_str[1] for sub_str in subrule_nums]
            if rule_num not in parsed_rules:
                parsed_rules[rule_num] = []
            parsed_rules[rule_num].append(subrule_nums)
    else:
        break


def test_rule(line, index, rule_num, rules):
    prev_pass = None
    rule = rules[rule_num]
    for option in rule:
        orig_index = index
        pass_opt = True
        for require in option:
            if isinstance(require, int):
                passed, steps = test_rule(line, index, int(require), rules)
                pass_opt = pass_opt and passed
                index = steps
            else:
                if index < len(line) and line[index] == require:
                    index += 1
                else:
                    pass_opt = False
            if not pass_opt:
                break

        if pass_opt:
#            if prev_pass is not None and prev_pass[0]:
#                print("oh crap")
            prev_pass = True, index

        index = orig_index

    if prev_pass is not None and prev_pass[0]:
        return prev_pass

    return pass_opt, index


for cur_line in content[line_num:]:
    cur_rules = parsed_rules
    cur_rules[8] = [[42]]
    cur_rules[11] = [[42, 31], [42, 11, 31]]
    result, end = test_rule(cur_line.strip(), 0, 0, cur_rules)
    count = 0
    while result is False and count < 10:
        cur_rules[8][0].append(42)
        result, end = test_rule(cur_line.strip(), 0, 0, cur_rules)
        count += 1

    if result and end == len(cur_line.strip()):
        part2 += 1

print("part 2 = " + str(part2))
