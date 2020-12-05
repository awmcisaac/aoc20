with open("input.txt") as f:
    passes = [line for line in f.read().strip().split("\n")]
    highest = 0
    seat_ids = []
    for line in passes:
        rowchars = 7
        rowlow = 0
        rowhigh = (2 ** rowchars) - 1
        colchars = 3
        collow = 0
        colhigh = (2 ** colchars) - 1
        for idx, elem in enumerate(line, 1):
            if elem == "F":
                rowhigh -= 2 ** (rowchars-idx)
            elif elem == "B":
                rowlow += 2 ** (rowchars-idx)
            elif elem == "L":
                colhigh -= 2 ** (colchars-idx+rowchars)
            elif elem == "R":
                collow += 2 ** (colchars-idx+rowchars)
        seat_ids += [rowlow * 8 + collow]
        if max(seat_ids) > highest:
            highest = max(seat_ids)
    print("Part 1:", highest)
    sorted_ids = sorted(seat_ids)
    for a, b in zip(sorted_ids, sorted_ids[1:]):
        if b - a == 2:
            print("Part 2:", a+1)
