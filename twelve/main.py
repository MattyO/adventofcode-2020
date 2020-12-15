from lib.computer import InstructionSet, instruction

class FerryInstructions(lib.computer.InstructionSet):

    @instruction('N')
    def north(i, world):
        pass

    @instruction('S')
    def south(i, world):
        pass

    @instruction('E')
    def east(i, world):
        pass

    def west(i, world):
        pass
    @instruction('L')
    def left(i, world):
        pass

    @instruction('R')
    def right(i, world):
        pass

    @instruction('F')
    def forward(i, world):
        pass

def ferry_parser(line):
    pass

FerryComputer = lib.computer.computer(
    instruction_set = FerryInstructions,
    world = {
        'direction': 'N', 
        'possition': (0,0),
    },
    parser = ferry_parser
    )

def find_location(filename):
    final_locaiton = None
    with open(filename) as f:
        fc = FerryComputer(f.readlines())
        fc.run()
        final_locaiton = fc.world['position']

    return final_locaiton

