import hashlib

input = "abc"
input = "ahsbgdzn"

md5Hash = ''
suffix = -1
keys = []
doing_part2 = True
cache = {}

while len(keys) < 64:
    suffix = suffix + 1
    if suffix % 1000 == 0:
        print(suffix)

    if suffix in cache:
        md5Hash = cache[suffix]
    else:
        h = hashlib.md5()
        hash_input = input + str(suffix)
        h.update(hash_input.encode('utf-8'))
        md5Hash = h.hexdigest()
        if doing_part2:
            for i in range(2016):
                h = hashlib.md5()
                hash_input = md5Hash
                h.update(hash_input.encode('utf-8'))
                md5Hash = h.hexdigest()
        cache[suffix] = md5Hash
    match_char = None
    for cur_index in range(len(md5Hash) - 2):
        if md5Hash[cur_index] == md5Hash[cur_index + 1] == md5Hash[cur_index + 2]:
            match_char = md5Hash[cur_index]

        if match_char is not None:
            for i in range(1, 1001):
                inner_suffix = suffix + i
                if inner_suffix in cache:
                    inner_md5Hash = cache[inner_suffix]
                else:
                    inner_h = hashlib.md5()
                    inner_hash_input = input + str(inner_suffix)
                    inner_h.update(inner_hash_input.encode('utf-8'))
                    inner_md5Hash = inner_h.hexdigest()
                    if doing_part2:
                        for inner_i in range(2016):
                            h = hashlib.md5()
                            hash_input = inner_md5Hash
                            h.update(hash_input.encode('utf-8'))
                            inner_md5Hash = h.hexdigest()
                    cache[inner_suffix] = inner_md5Hash

                if "".join([match_char] * 5) in inner_md5Hash:
                    keys.append((suffix, i, inner_suffix, match_char, md5Hash))
                    break
            break

print("Part 1 = " + str(suffix))
# print("Part 2 = " + "".join(part2))
