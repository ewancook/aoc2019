
import itertools
intcodes = [int(x) for x in open("input.txt").readline().rstrip("\n").split(",")]

def totalise_instructions(codes, cell_one, cell_two):
    codes[1:3] = cell_one, cell_two
    i = 0
    while i < len(codes):
        op, first, second, pos = codes[i:i+4]
        if op == 99:
            return codes[0]
        codes[pos] = codes[first]+codes[second] if op%2 else codes[first]*codes[second]
        i += 4

print("Part 1:", totalise_instructions(intcodes[:], 12, 2))

for a, b in itertools.permutations(range(100), 2):
        if totalise_instructions(intcodes[:], a, b) == 19690720:
            print("Part 2:", 100*a + b)
            break
