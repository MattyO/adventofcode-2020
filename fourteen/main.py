import lib.matcher
from lib.computer import Instruction, instruction, Computer, InstructionSet

def parse(filename):
    def mask_instruction(result):
        return Instruction("mask", result.operand)
    def mem_instruction(result):
        return Instruction("mem", (int(result.address), int(result.operand)))

    instructions = []
    lines = None
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        #result = match_list({
        #    'mask': "mask = <operand:[X10]+",
        #    'men': "mem[<address:int>] = <operand:int>",
        #    })
        result = lib.matcher.match("<operation:mask|mem>[\[]*<address:[0-9]*>[\]]* = <operand:[X0-9]+>", line)

        instructions.append({
            'mask':mask_instruction ,
            'mem': mem_instruction,
            }[result.operation](result))


    return instructions

def mask(value, mask):
    char_array = list(value)
    for i, c in enumerate(mask):
        if c != 'X':
            char_array[i] = c

    return "".join(char_array)

class DockingInstructionSet(InstructionSet):
    world = {
        'memory':{},
        'mask': None,
    }
    @instruction('mem')
    def mem(self, instruction, world):
        address, num = instruction.argument
        binary_num = bin(num)[2:].rjust(36, "0")
        world['memory'][address] = int(mask(binary_num , world['mask']),2)
        return world

    @instruction('mask')
    def mask(self, instruction, world):
        world['mask'] = instruction.argument
        return world

PartOneComputer = Computer(
    instruction_set = DockingInstructionSet(),
    world = {
        'memory':{},
        'mask': None,
    }
)


def address_sum(comp):
    return sum(v for k, v in comp.world['memory'].items())




