from collections import defaultdict, namedtuple
from itertools import cycle, izip

from intcode import parse_intcode

vec = namedtuple("vec", ["x", "y"])

mov = [
    lambda v: vec(v.x, v.y+1),
    lambda v: vec(v.x+1, v.y),
    lambda v: vec(v.x, v.y-1),
    lambda v: vec(v.x-1, v.y)
]

dirs = ["U", "R", "D", "L"]

def paint(input, start_colour):
    pos, args, dir = vec(0, 0), [start_colour], 0
    positions = defaultdict(vec, {pos:start_colour})
    for colour, value in izip(cycle([1, 0]), parse_intcode(input, args)):
        if colour:
            positions[pos] = value
        else:
            dir = dirs.index(dirs[(dir+[-1,1][value])%len(dirs)])
            pos = mov[dir](pos)
            args.append(positions.get(pos, 0))
    return positions

input = [int(i) for i in open("input.txt").readline().strip().split(",")]
print("Part One:", len(paint(input, 0).keys()))

part_two = paint(input, 1)
x, y, keys = lambda k: k.x, lambda k: k.y, part_two.keys()
min_x, max_x = min(keys, key=x).x, max(keys, key=x).x
min_y, max_y = min(keys, key=y).y, max(keys, key=y).y

coloured = {
    0: '\x1b[0;30;40m]0\x1b[0m',
    1: '\x1b[6;37;47m]1\x1b[0m',
}

for y in range(max_y, min_y-1, -1):
    row = [coloured[part_two.get(vec(x, y), 0)] for x in range(min_x, max_x)]
    print("".join(row))
