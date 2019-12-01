with open("input7.txt") as f:
    content = f.readlines()

support_tls = 0
support_ssl = 0
hypernet = False

for cur_line in content:
    cur_tls = False
    no_tls = False
    cur_ssl = False
    hypernet_abas = []
    supernet_abas = []

    for char_index, cur_char in enumerate(cur_line):
        if cur_char == '[':
            hypernet = True
        if cur_char == ']':
            hypernet = False

        # ABBA / tls
        if char_index + 3 < len(cur_line):
            if cur_char == cur_line[char_index + 3] and cur_line[char_index + 1] == cur_line[
                char_index + 2] and cur_char != cur_line[char_index + 2]:
                if hypernet:
                    no_tls = True
                else:
                    cur_tls = True

        # ABA / ssl
        if char_index + 2 < len(cur_line):
            if cur_char == cur_line[char_index + 2] and cur_line[char_index + 1] != cur_char:
                aba = (cur_char, cur_line[char_index + 1])
                if hypernet:
                    hypernet_abas.append(aba)
                else:
                    supernet_abas.append(aba)

    if cur_tls and not no_tls:
        support_tls += 1

    for aba in supernet_abas:
        if (aba[1], aba[0]) in hypernet_abas:
            cur_ssl = True

    if cur_ssl:
        support_ssl += 1

print("part 1 = " + str(support_tls))
print("part 2 = " + str(support_ssl))
