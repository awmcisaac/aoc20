import math
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    pointers = [0,0,0,0,0]
    moves = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    trees = [0,0,0,0,0]
    for i, move in enumerate(moves):
        for idx, line in enumerate(lines):
            if idx % move[1] == 0:
                if line[pointers[i]] == "#":
                    trees[i] += 1
                pointers[i] = (pointers[i] + move[0]) % len(line)
    print(math.prod(trees))
