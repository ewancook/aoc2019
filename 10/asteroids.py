from math import atan2, sqrt, pi
from collections import namedtuple

vec = namedtuple("vec", ["x", "y"])

def angle(a, b):
    return pi/2 + atan2(a.y-b.y, a.x-b.x)

def dist(a, b):
    return sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def part_one(asteroids):
    angles = {a: [angle(a, b) for b in asteroids if a != b] for a in asteroids}
    base = max(angles.keys(), key=lambda k: len(set(angles[k])))
    return len(set(angles[base])), base

def part_two(asteroids, base):
    angles_around_base = {angle(a, base): sorted([(a, dist(a, base))]) for a in asteroids if a != base}
    keys = sorted(angles_around_base.keys())
    first_minus = keys.index(max([i for i in keys if i < 0]))
    keys = keys[first_minus+1:] + keys[:first_minus+1]

    vapourised = [angles_around_base[angle].pop(0) for angle in keys][199][0]
    return vapourised.x*100 + vapourised.y, vapourised


asteroids = []
with open("input.txt") as lines:
    for y, line in enumerate(lines.readlines()):
        for x, c in enumerate(list(line)):
            if c == '#':
                asteroids.append(vec(x, y))

count, base = part_one(asteroids)
print("Part One: {} ({})".format(count, base))
print("Part Two: {} ({})".format(*part_two(asteroids, base)))
