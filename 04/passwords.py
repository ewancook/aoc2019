lower, upper = [int(x) for x in open("input.txt").readline().split("-")]

part_one, part_two = 0, 0
for i in range(lower, upper+1):
    l = list(str(i))
    if sorted(l) == l and len(l) != len(set(l)):
        part_one += 1
        part_two += 1 if 2 in [l.count(v) for v in set(l)] else 0

print("Part 1: {}; Part 2: {}".format(part_one, part_two))
