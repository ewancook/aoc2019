from itertools import combinations
from copy import deepcopy
from math import gcd

initial_moons = [
    [[10, 15, 7], [0, 0, 0]],
    [[15, 10, 0], [0, 0, 0]],
    [[20, 12, 3], [0, 0, 0]],
    [[0, -3, 13], [0, 0, 0]],
]

def lcm(l):
    mult = l[0]
    for v in l[1:]:
        mult = mult*v//gcd(mult, v)
    return mult

def add_comp(v):
    return sum([abs(i) for i in v[:3]])

def change_velocities(a, b, axis):
    if a[0][axis] != b[0][axis]:
        new_a = 1 if a[0][axis] < b[0][axis] else -1
        new_b = -1 if new_a > 0 else 1
        a[1][axis] += new_a
        b[1][axis] += new_b

def step(moons):
    for axis in range(3):
        for a, b in combinations(moons, 2):
            change_velocities(a, b, axis)
        for m, v in moons:
            m[axis] += v[axis]

moons = deepcopy(initial_moons)
for time_step in range(1000):
    step(moons)

time_step = 0
pos_start = [[m[0][a] for m in initial_moons] for a in range(3)]
steps_from_start = [0]*3

while 0 in steps_from_start:
    for axis in range(3):
        pos, vel = [], []
        for m in initial_moons:
            pos.append(m[0][axis])
            vel.append(m[1][axis])
        if all([pos == pos_start[axis], vel == [0]*4, not steps_from_start[axis]]):
            steps_from_start[axis] = time_step
    step(initial_moons)
    time_step += 1

print("Part One:", sum(add_comp(m)*add_comp(v) for m, v in moons))
print("Part Two:", lcm(steps_from_start))
