import hashlib

# input = "abc"
input = "ugkcyxxp"

md5Hash = ''
suffix = -1
part1 = []
part2 = ['.'] * 8

while '.' in part2:
    suffix = suffix + 1
    h = hashlib.md5()
    hash_input = input + str(suffix)
    h.update(hash_input.encode('utf-8'))
    md5Hash = h.hexdigest()
    if md5Hash.startswith("00000"):
        if len(part1) < 8:
            part1.append(md5Hash[5])

        try:
            pwd_index = int(md5Hash[5])
            if pwd_index < 8:
                if part2[pwd_index] == '.':
                    part2[pwd_index] = md5Hash[6]
                    print(md5Hash)
        except ValueError:
            continue

print("Part 1 = " + "".join(part1))
print("Part 2 = " + "".join(part2))
