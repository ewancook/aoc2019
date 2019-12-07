class Parser:
    def __init__(self, instructions, inputs):
        self.instr = instructions
        self.inputs = inputs
        self.pos = 0
        self.basic_instructions = {
                1: self.add,
                2: self.multiply,
                3: self.take_input,
                4: self.output,
                5: self.jump_if_true,
                6: self.jump_if_false,
                7: self.less_than,
                8: self.equals,
                99: self.end
        }

    def get_value(self, value, mode):
        return value if mode else self.instr[value]

    def add(self, m1, m2):
        a, b, dest = self.instr[self.pos+1:self.pos+4]
        self.instr[dest] = self.get_value(a, m1)+self.get_value(b, m2)
        if dest != self.pos:
            self.pos += 4

    def multiply(self, m1, m2):
        a, b, dest = self.instr[self.pos+1:self.pos+4]
        self.instr[dest] = self.get_value(a, m1)*self.get_value(b, m2)
        if dest != self.pos:
            self.pos += 4

    def take_input(self, m1, m2):
        dest = self.instr[self.pos+1]
        self.instr[dest] = self.inputs.pop()
        if dest != self.pos:
            self.pos += 2

    def output(self, pos, m1, m2=0):
        dest = self.instr[self.pos+1]
        self.pos += 2
        return self.get_value(dest, m1)

    def jump_if_true(self, m1, m2):
        a, b = self.instr[self.pos+1:self.pos+3]
        if self.get_value(a, m1) != 0:
            self.pos = self.get_value(b, m2)
        else:
            self.pos += 3

    def jump_if_false(self, m1, m2):
        a, b = self.instr[self.pos+1:self.pos+3]
        if self.get_value(a, m1) == 0:
            self.pos = self.get_value(b, m2)
        else:
            self.pos += 3

    def less_than(self, m1, m2):
        a, b, dest = self.instr[self.pos+1:self.pos+4]
        self.instr[dest] = self.get_value(a, m1) < self.get_value(b, m2)
        if dest != self.pos:
            self.pos += 4

    def equals(self, m1, m2):
        a, b, dest = self.instr[self.pos+1:self.pos+4]
        self.instr[dest] = self.get_value(a, m1) == self.get_value(b, m2)
        if dest != self.pos:
            self.pos += 4

    def end(self, m1, m2):
        self.pos = len(self.instr)

    def parse(self):
        while self.pos < len(self.instr):
            s = str(self.instr[self.pos]).zfill(4)
            op, a, b = int(s[2:]), int(s[1]), int(s[0])
            out = self.basic_instructions[op](a, b)
            if out is not None:
                return out
