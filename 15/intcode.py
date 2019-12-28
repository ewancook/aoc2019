from collections import defaultdict


def parse_intcode(instructions, inputs):
    pos, r_base = 0, 0
    ins = defaultdict(int, {k: v for k, v in enumerate(instructions)})
    sizes = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    while True:
        op = ins[pos] % 100
        if op == 99:
            return
        size = sizes[op]
        modes = [(ins[pos] // 10**i) % 10 for i in range(2, 5)]
        args = [ins[a] for a in range(pos + 1, pos + size)]
        params, dests = [], []
        for arg, m in zip(args, modes):
            params.append((ins[arg], arg, ins[arg + r_base])[m])
            dests.append((arg, arg, arg + r_base)[m])
        pos += size
        if op == 1:
            ins[dests[2]] = sum(params[:2])
        elif op == 2:
            ins[dests[2]] = params[0] * params[1]
        elif op == 3:
            ins[dests[0]] = inputs.pop(0)
        elif op == 4:
            yield params[0]
        elif op == 5 and params[0] != 0:
            pos = params[1]
        elif op == 6 and not params[0]:
            pos = params[1]
        elif op == 7:
            ins[dests[2]] = params[0] < params[1]
        elif op == 8:
            ins[dests[2]] = params[0] == params[1]
        elif op == 9:
            r_base += params[0]
