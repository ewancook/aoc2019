from itertools import permutations, cycle
from opcodes import Parser

def part_one(input):
    outputs = []
    for perm in permutations(range(5), 5):
        last_input = 0
        for amp in [Parser(input, [p]) for p in perm]:
            amp.inputs.insert(0, last_input)
            last_input = amp.parse()
        outputs.append(last_input)
    return max(outputs)

def part_two(input):
    outputs = []
    for perm in permutations(range(5, 10), 5):
        amps = cycle([Parser(input, [p]) for p in perm])
        last_input = 0
        for i, amp in enumerate(amps):
            amp.inputs.insert(0, last_input)
            output = amp.parse()
            if output is None:
                if i%5 == 4:
                    break
                continue
            last_input = output
        outputs.append(last_input)
    return max(outputs)


input = [int(i) for i in open("input.txt").readline().strip().split(",")]
print(part_one(input))
print(part_two(input))
