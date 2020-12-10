def run(lines):
    visited = set()
    pos = 0
    accum_val = 0
    while pos < len(lines):
        if pos in visited: # no new position was visited
#            print("Part 1:", accum_val)
            return None
        visited.add(pos)
        if lines[pos][0] == "nop":
            pos += 1
        elif lines[pos][0] == "acc":
            accum_val += int(lines[pos][1])
            pos += 1
        elif lines[pos][0] == "jmp":
            pos += int(lines[pos][1])

    return accum_val

with open("input.txt") as f:
    lines = [line.rstrip('\n').split(" ") for line in f.readlines()]
    lines = [(op, int(x)) for op, x in lines]
    
    for i in range(len(lines)):
        if lines[i][0] == "acc":
            continue
        new_op = "jmp" if lines[i][0] == "nop" else "nop"
        new_lines = lines[:i] + [[new_op, lines[i][1]]] + lines[i+1:]
        x = run(new_lines)
        if x is not None:
            print("Part 2:", x)             
