import ast
import math

with open("input18.txt") as f:
    content = f.readlines()

part2 = 0


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


for line_num, line in enumerate(content):
    content[line_num] = ast.literal_eval(content[line_num])


def read_num(exp_str):
    num_index = 0
    num_str = ""
    while exp_str[num_index].isdigit():
        num_str += exp_str[num_index]
        num_index += 1
    return int(num_str)


def parse_expression(expr):
    cur_node = Node()
    if isinstance(expr, int):
        cur_node.data = expr
    else:
        if isinstance(expr, list):
            cur_node.left = parse_expression(expr[0])
            cur_node.right = parse_expression(expr[1])

    return cur_node


def print_tree(expr_tree, depth=0):
    if expr_tree.data is not None:
        print(expr_tree.data, end='')
    else:
        print('[', end='')
        print_tree(expr_tree.left, depth + 1)
        print(',', end='')
        print_tree(expr_tree.right, depth + 1)
        print(']', end='')

    if depth == 0:
        print()


last_num = None
exploded_second = None


def explode(exp_tree, depth=0):
    global last_num
    global exploded_second

    if depth == 0:
        last_num = None
        exploded_second = None

    if exp_tree is None:
        return False

    if exp_tree.data is not None:
        if exploded_second is not None:
            exp_tree.data += exploded_second
            return True
        else:
            last_num = exp_tree

    if exp_tree.left is not None and exp_tree.left.data is not None:
        if depth > 3 and exploded_second is None:
#            print((exp_tree.left.data, exp_tree.right.data))
            if last_num is not None:
                last_num.data += exp_tree.left.data
            exploded_second = exp_tree.right.data

            exp_tree.left = None
            exp_tree.right = None
            exp_tree.data = 0

    return explode(exp_tree.left, depth + 1) or explode(exp_tree.right, depth + 1)


def split(exp_tree):
    if exp_tree is None:
        return False

    if exp_tree.data is not None and exp_tree.data > 9:
        #print(exp_tree.data)
        left_node = Node(math.floor(exp_tree.data / 2), None, None)
        right_node = Node(math.ceil(exp_tree.data / 2), None, None)
        exp_tree.data = None
        exp_tree.left = left_node
        exp_tree.right = right_node
        return True

    return split(exp_tree.left) or split(exp_tree.right)


def calculate_magnitude(exp_tree):
    if exp_tree is None:
        return 0
    if exp_tree.data is not None:
        return exp_tree.data
    return 3 * calculate_magnitude(exp_tree.left) + 2 * calculate_magnitude(exp_tree.right)


# addition
expression_trees = []
for line_num, line in enumerate(content):
    expression_trees.append(parse_expression(line))

max_mag = 0
for first_index, first_tree in enumerate(content):
    for second_index, second_tree in enumerate(content):
        if first_index == second_index:
            continue

        add_tree = Node(None, parse_expression(first_tree), parse_expression(second_tree))
        counter = 0
        while explode(add_tree) or split(add_tree):
            #print_tree(add_tree)
            counter += 1

        mag = calculate_magnitude(add_tree)
        max_mag = max(mag, max_mag)

part2 = max_mag
print("part 2 = " + str(part2))