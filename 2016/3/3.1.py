with open("input3.txt") as f:
    content = f.readlines()

possible_count = 0
for cur_line in content:
    nums = [val for val in cur_line.strip().split(' ') if not len(val) < 1]
    nums = [int(val) for val in nums]
    nums.sort()

    if nums[0] + nums[1] > nums[2]:
        possible_count += 1

print(possible_count)
