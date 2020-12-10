with open("input.txt") as f:
    nums = sorted([int(i) for i in f.read().strip().split("\n")])

    one_diffs = 0
    two_diffs = 0
    three_diffs = 0
    built_in_adapter = 3 + max(nums)
    outlet = 0
    nums = [outlet] + nums + [built_in_adapter]
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] == 1:
            one_diffs += 1
        elif nums[i+1] - nums[i] == 2:
            two_diffs += 1
        else: # nums[i+1] - nums[i] == 3:
            three_diffs += 1
    print("Part 1:", one_diffs * three_diffs)
    
    perms = 1
    pointer = 0
    coefs = [1,1,2,4,7,13,24] # tribonacci numbers!
    for (idx, (a,b)) in enumerate(zip(nums, nums[1:])):
        if b - a == 3:
            perms *= coefs[idx-pointer]
            pointer = idx+1
    print("Part 2:", perms)
