with open("input.txt") as f:
    nums = [int(i) for i in f.read().strip().split("\n")]
    window = []
    window_size = 25
    for num in nums:
        if len(window) == window_size:
            if all(num - elem not in window[:idx] + window[idx+1:] for idx, elem in enumerate(window)):
                invalid = num
                print("Part 1:", invalid)
            window.pop(0)
        if len(window) < window_size:
            window += [num]
    
    # part 2
    invalid = invalid
    contig = []
    for num in nums:
        if sum(contig) == invalid and len(contig) != 1:
            print("Part 2:", min(contig) + max(contig))
        elif sum(contig) > invalid:
            while sum(contig) > invalid:
                contig.pop(0)
        contig += [num]
