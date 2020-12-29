import lib.matcher
from lib.computer import Instruction, instruction, Computer, InstructionSet
import itertools

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

def mask(value, mask, ignore=['X']):
    char_array = list(value)
    for i, c in enumerate(mask):
        if c not in ignore:
            char_array[i] = c

    return "".join(char_array)

def possible_addresses(address):
    r_addresses = []
    x_possitions = [ i for i,c in enumerate(address) if c == 'X']
    possible_values = list(itertools.product(['1','0'], repeat=len(x_possitions)))

    for p_values in possible_values:
        current_address_array = list(address)
        values_and_positions = zip(p_values, x_possitions, )

        for value, position,  in values_and_positions:
            current_address_array[position] = value

        r_addresses.append("".join(current_address_array))

    return r_addresses


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

class DockingInstructionSet2(InstructionSet):
    world = {
        'memory':{},
        'mask': None,
    }
    @instruction('mem')
    def mem(self, instruction, world):
        address, num = instruction.argument
        binary_address = bin(address)[2:].rjust(36, "0")
        masked_binary_address = mask(binary_address, world['mask'], ignore=['0'])
        for str_address in possible_addresses(masked_binary_address):
            int_address = int(str_address, 2)
            world['memory'][int_address] = num

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

PartTwoComputer = Computer(
    instruction_set = DockingInstructionSet2(),
    world = {
        'memory':{},
        'mask': None,
    }
)


def address_sum(comp):
    return sum(v for k, v in comp.world['memory'].items())




