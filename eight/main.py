import collections 
import lib.matcher
from pprint import pprint
import copy

class Instruction():
    def __init__(self, operation, argument, run_at=None):
        self.operation = operation
        self.argument = argument
        self.run_at = run_at

    def __repr__(self):
        return f"{self.operation} {self.argument} | {self.run_at}"


def parse(filename):
    instructions = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        m = lib.matcher.match("<operation:string> <argument:[\+\-][0-9]+>", line)
        instructions.append(Instruction(m.operation, int(m.argument)))

    return instructions

class Comp():
    def __init__(self, accumulator=0):
        self.accumulator = accumulator
        self.index = 0

    def run(self, instructions):
        self.index = 0
        self.accumulator = 0
        has_finished = True
        counter = 0
        while self.index < len(instructions):
            instruction = instructions[self.index]
            if instruction.run_at is not None:
                has_finished = False
                break;
            self.run_instruction(instruction)
            counter += 1
            instruction.run_at = counter
        #pprint(instructions)

        return has_finished

    def nop(self, arg):
        self.index += 1

    def acc(self, arg):
        self.accumulator+=arg
        self.index += 1

    def jump(self, arg):
        self.index += arg

    def run_instruction(self, instruction):
        return {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jump,
        }.get(instruction.operation)(instruction.argument)

def fix(instructions):
    c = Comp()
    for i, instruction in enumerate(instructions):
        if instruction.operation == 'acc':
            continue
        new_instruction = copy.deepcopy(instruction)
        new_instruction.operation  = { 'jmp': 'nop', 'nop': 'jmp'}[instruction.operation]
        new_instructions = copy.deepcopy(instructions)
        new_instructions[i] = new_instruction
        if c.run(new_instructions) == True:
            return c

    return None



