with open("test_input18.txt") as f:
    content = f.readlines()

part2 = 0


def do_math_expr(expr):
    for op in "+*":
        while op in expr:
            op_ind = expr.index(op)
            if op == "+":
                new_val = expr[op_ind - 1] + expr[op_ind + 1]
            else:
                if op == "*":
                    new_val = expr[op_ind - 1] * expr[op_ind + 1]
            expr = expr[:op_ind - 1] + [new_val] + expr[op_ind + 2:]
    return expr[0]


def do_math_line(expr):
    op = ""
    indx = 0
    new_expr = []
    while indx < len(expr):
        piece = expr[indx]
        if piece == " ":
            indx += 1
            continue
        if piece == "+" or piece == "*":
            new_expr.append(piece)
        else:
            if piece == ")":
                return (do_math_expr(new_expr), indx)
            if piece == "(":
                (val, steps) = do_math_line(expr[indx + 1:])
                new_expr.append(val)
                indx += steps + 1
            else:
                new_expr.append(int(piece))
            if piece in "+*":
                new_expr.append(op)
        indx += 1

    return do_math_expr(new_expr), indx


for cur_line in content:
    expr = cur_line.strip()
    line_sum = do_math_line(expr)
    part2 += line_sum[0]

print("part 2 = " + str(part2))
