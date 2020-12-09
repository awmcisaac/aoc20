import re
import collections

with open("input.txt") as f:
    data = f.read().strip().split("\n")
    contained_in = collections.defaultdict(set)
    contains = collections.defaultdict(list)
    for line in data:
        colour = re.match(r'(.+?) bags contain', line)[1]
        for cnt, inner_colour in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            cnt = int(cnt)
            contained_in[inner_colour].add(colour)
            contains[colour].append((cnt, inner_colour))

    holds_gold = set()
    def check(colour):
        for c in contained_in[colour]:
            holds_gold.add(c)
            check(c)
    check('shiny gold')
    print("Part 1:", len(holds_gold))

    def cost(colour):
        total = 0
        for cnt, inner_colour in contains[colour]:
            total += cnt
            total += cnt * cost(inner_colour)
        return total
    print("Part 2:", cost('shiny gold'))
