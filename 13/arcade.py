from collections import defaultdict

from intcode import parse_intcode

input = [int(i) for i in open("input.txt").readline().strip().split(",")]
m = defaultdict(dict, {})

code = parse_intcode(input, [])
for x in code:
    y = next(code)
    t = ["", "|", "#", "_", "o"][next(code)]
    m[y][x] = t

cursor, score, joystick = 0, 0, []
code = parse_intcode([2]+input[1:], joystick)
for x in code:
    y = next(code)
    t = next(code)
    if [x, y] == [-1, 0]:
        score = t
    else:
        if t == 4:
            joystick.append(0 if x == cursor else -1 if x < cursor else 1)
        elif t == 3:
            cursor = x

print("Part One:", [t for x in m.values() for t in x.values()].count("#"))
print("Part Two:", score)
