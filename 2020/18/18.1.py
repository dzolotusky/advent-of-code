with open("input18.txt") as f:
    content = f.readlines()

part1 = 0


def do_math(expr, cur_val):
    op = ""
    indx = 0
    while indx < len(expr):
        piece = expr[indx]
        if piece == " ":
            indx += 1
            continue
        if piece == "+" or piece == "*":
            op = piece
        else:
            if piece == ")":
                return cur_val, indx
            if piece == "(":
                (val, steps) = do_math(expr[indx + 1:], 0)
                indx += steps + 1
            else:
                val = int(piece)
            if op == "+":
                cur_val += val
            else:
                if op == "*":
                    cur_val *= val
                else:
                    cur_val = val
        indx += 1

    return cur_val, indx


for cur_line in content:
    expr = cur_line.strip()
    line_sum = do_math(expr, 0)
    part1 += line_sum[0]

print("part 1 = " + str(part1))
