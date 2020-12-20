from lib.computer import InstructionSet, instruction, Computer, Instruction

class FerryInstructions(InstructionSet):
    world = {
        'direction': 90, 
        'position': (0,0),
    }

    @instruction('N')
    def north(self, i, world):
        x, y = world['position']
        world['position'] = (x, y+i.argument)
        return world

    @instruction('S')
    def south(self, i, world):
        x, y = world['position']
        world['position'] = (x, y-i.argument)
        return world

    @instruction('E')
    def east(self, i, world):
        x, y = world['position']
        world['position'] = (x+i.argument, y)
        return world

    @instruction('W')
    def west(self, i, world):
        x, y = world['position']
        world['position'] = (x-i.argument, y)
        return world

    @instruction('L')
    def left(self, i, world):
        temp = world['direction'] - i.argument
        while temp < 0:
            temp += 360

        world['direction'] = temp
        return world

    @instruction('R')
    def right(self, i, world):
        temp = world['direction'] + i.argument
        while temp >= 360:
            temp -= 360

        world['direction'] = temp
        return world

    @instruction('F')
    def forward(self, i, world):
        direction_map ={
            0: self.north,
            90: self.east,
            180: self.south,
            270: self.west,
        }
        return direction_map[world['direction']](i, world)

def ferry_parser(filename):
    lines = None
    with open(filename) as f:
        lines = f.read().splitlines()

    return [ Instruction(i[0], int(i[1:])) for i in lines ]

FerryComputer = Computer(
    instruction_set = FerryInstructions(),
    world = {'direction': 90}
)


def find_location(filename):
    fc = FerryComputer()
    fc.run(ferry_parser(filename))
    return fc.world['position']

