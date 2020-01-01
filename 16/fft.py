def gen_phase(l, r):
    repeat, size = [a for x in [0, 1, 0, -1] for a in [x] * r], 4 * r
    if l < size:
        return repeat[1:l + 1]
    else:
        a, b = divmod(l - size + 1, size)
        return repeat[1:] + a * repeat + repeat[:b]


def step_first(l, phases):
    return [abs(sum([l[a] * b for a, b in enumerate(phases[i])])) %
            10 for i, x in enumerate(l)]


def step_second(l, offset):
    for x in range(len(l) - 2, offset - 1, -1):
        l[x] = (l[x] + l[x + 1]) % 10


def _l_to_int(l):
    return int("".join(str(i) for i in l))


first = [int(i) for i in open("input.txt").readline().strip()]
second = first * 10000
pos = _l_to_int(second[:7])
phases = [gen_phase(len(first), i + 1) for i in range(len(first) + 1)]
for i in range(100):
    first = step_first(first, phases)
    step_second(second, pos)

print("Part One: {}".format(_l_to_int(first[:8])))
print("Part Two: {}".format(_l_to_int(second[pos:pos + 8])))
