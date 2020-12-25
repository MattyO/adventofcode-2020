from lib.computer import InstructionSet, instruction, Computer, Instruction

class SharedInstructions():
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


class FerryInstructions(InstructionSet, SharedInstructions):
    world = {
        'direction': 90, 
        'position': (0,0),
    }

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

class FerryInstructions2(InstructionSet, SharedInstructions):
    world = {
        'position': (0,0),
        'ship_position': (0,0),
    }

    @instruction('L')
    def left(self, i, world):
        num_turns = int(i.argument / 90)
        new_position = world['position']

        while num_turns > 0:
            x,y = new_position
            new_position  = (-1 * y,  x)
            num_turns -= 1

        world['position'] = new_position

        return world

    @instruction('R')
    def right(self, i, world):

        num_turns = int(i.argument / 90)
        new_position = world['position']

        while num_turns > 0:
            x,y = new_position
            new_position  = (y, -1 * x)
            num_turns -= 1

        world['position'] = new_position

        return world

    @instruction('F')
    def forward(self, i, world):
        x, y = world['position']
        ship_x, ship_y = world['ship_position']

        world['ship_position'] = ((x * i.argument) + ship_x, (y * i.argument) + ship_y)

        return world

def ferry_parser(filename):
    lines = None
    with open(filename) as f:
        lines = f.read().splitlines()

    return [ Instruction(i[0], int(i[1:])) for i in lines ]

FerryComputer = Computer(
    instruction_set = FerryInstructions(),
    world = {'direction': 90}
)

FerryComputer2 = Computer(
    instruction_set = FerryInstructions2(),
    world = {
        'position': (10,1),
        'ship_position': (0,0),
    }
)

def find_location(filename):
    fc = FerryComputer()
    fc.run(ferry_parser(filename))
    return fc.world['position']

def find_location2(filename):
    fc = FerryComputer2()
    fc.run(ferry_parser(filename))
    return fc.world['ship_position']
