with open("input3.txt") as f:
    content = f.readlines()

possible_count = 0
potentials = []
in_progress = [[], [], []]

for cur_line in content:
    nums_on_line = [val for val in cur_line.strip().split(' ') if not len(val) < 1]
    for num_index, num in enumerate(nums_on_line):
        in_progress[num_index].append(num)

    if len(in_progress[0]) == 3:
        potentials = potentials + in_progress
        in_progress = [[], [], []]

for nums in potentials:
    nums = [int(val) for val in nums]
    nums.sort()

    if nums[0] + nums[1] > nums[2]:
        possible_count += 1

print(possible_count)
