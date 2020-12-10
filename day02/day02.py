with open("input.txt") as f:
    lines = [i.replace(":", '').replace("-", " ").rstrip().split(" ") for i in f.readlines()]
# part 1
    valid = 0
    for line in lines:
        char_count = 0
        for char in line[3]:
            if char == line[2]:
                char_count += 1
        if int(line[0]) <= char_count and int(line[1]) >= char_count:
            valid += 1
    print("Part 1 valid: ", valid)

# part 2
    valid = 0
    for line in lines:
        idx1 = int(line[0])-1
        idx2 = int(line[1])-1
        if bool(line[3][idx1] == line[2]) ^  bool(line[3][idx2] == line[2]):
            valid += 1
    print("Part 2 valid: ", valid)

        
