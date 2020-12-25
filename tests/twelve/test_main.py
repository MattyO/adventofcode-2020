import unittest
import twelve.main
from lib.computer import Instruction

class FerryInstructionsTest(unittest.TestCase):

    def test_north(self):
        starting_world = { 'position': (0,0) }
        north_instruction = Instruction('N', 20)
        expected_world = twelve.main.FerryInstructions().north(north_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (0, 20)}) 


    def test_south(self):
        starting_world = { 'position': (0,0) }
        south_instruction = Instruction('S', 20)
        expected_world = twelve.main.FerryInstructions().south(south_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (0, -20)}) 

    def test_east(self):
        starting_world = { 'position': (0,0) }
        east_instruction = Instruction('E', 20)
        expected_world = twelve.main.FerryInstructions().east(east_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (20, 0)}) 

    def test_west(self):
        starting_world = { 'position': (0,0) }
        west_instruction = Instruction('W', 20)
        expected_world = twelve.main.FerryInstructions().west(west_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (-20, 0)}) 

    def test_left(self):
        starting_world = { 'direction': 0 }
        left_instruction = Instruction('L', 90)
        expected_world = twelve.main.FerryInstructions().left(left_instruction, starting_world)
        self.assertEqual(expected_world, {'direction': -90}) 

    def test_right(self):
        starting_world = { 'direction': 0 }
        right_instruction = Instruction('R', 90)
        expected_world = twelve.main.FerryInstructions().right(right_instruction, starting_world)
        self.assertEqual(expected_world, {'direction': 90}) 

    def test_right_greater_than_360(self):
        starting_world = { 'direction': 180 }
        right_instruction = Instruction('R', 270 )
        expected_world = twelve.main.FerryInstructions().right(right_instruction, starting_world)
        self.assertEqual(expected_world, {'direction': 90}) 

    def test_right_less_than_0(self):
        starting_world = { 'direction': 0 }
        right_instruction = Instruction('L', 90)
        expected_world = twelve.main.FerryInstructions().left(right_instruction, starting_world)
        self.assertEqual(expected_world, {'direction': 270}) 

    def test_forward_direction_0(self):
        starting_world = { 'position': (0,0), 'direction': 0 }
        forward_instruction = Instruction('F', 20)
        expected_world = twelve.main.FerryInstructions().forward(forward_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (0, 20), 'direction': 0}) 

    def test_forward_direction_90(self):
        starting_world = { 'position': (0,0), 'direction': 90 }
        forward_instruction = Instruction('F', 20)
        expected_world = twelve.main.FerryInstructions().forward(forward_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (20, 0), 'direction': 90}) 

    def test_forward_direction_180(self):
        starting_world = { 'position': (0,0), 'direction': 180 }
        forward_instruction = Instruction('F', 20)
        expected_world = twelve.main.FerryInstructions().forward(forward_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (0, -20), 'direction': 180}) 

    def test_forward_direction_270(self):
        starting_world = { 'position': (0,0), 'direction': 270}
        forward_instruction = Instruction('F', 20)
        expected_world = twelve.main.FerryInstructions().forward(forward_instruction, starting_world)
        self.assertEqual(expected_world, {'position': (-20, 0), 'direction': 270}) 

    def test_find_instruction(self):
        #TODO: mmove to lib test
        self.assertEqual(
            twelve.main.FerryInstructions().get_instruction("N").__name__,
            "north"
        )

    def test_find_instruction_south(self):
        #TODO: mmove to lib test
        self.assertEqual(
            twelve.main.FerryInstructions().get_instruction("S").__name__,
            "south"
        )

class FerryInstructions2Test(unittest.TestCase):

    def test_test_right(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        right_instruction = Instruction('R', 90)
        expected_world = twelve.main.FerryInstructions2().right(right_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (4,-10)} ) 

    def test_right_180(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        right_instruction = Instruction('R', 180)
        expected_world = twelve.main.FerryInstructions2().right(right_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (-10, -4)} ) 

    def test_right_270(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        right_instruction = Instruction('R', 270)
        expected_world = twelve.main.FerryInstructions2().right(right_instruction , starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (-4,10)} ) 

    def test_right_360(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        right_instruction = Instruction('R', 360)
        expected_world = twelve.main.FerryInstructions2().right(right_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (10,4)} ) 

    def test_left(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        left_instruction = Instruction('L', 90)
        expected_world = twelve.main.FerryInstructions2().left(left_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (-4,10)} ) 

    def test_left_180(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        left_instruction = Instruction('L', 180)
        expected_world = twelve.main.FerryInstructions2().left(left_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (-10,-4)} ) 

    def test_left_270(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        left_instruction = Instruction('L', 270)
        expected_world = twelve.main.FerryInstructions2().left(left_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (4,-10)} ) 

    def test_left_360(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        left_instruction = Instruction('L', 360)
        expected_world = twelve.main.FerryInstructions2().left(left_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (0,0), 'position': (10,4)} ) 

    def test_forward(self):
        starting_world = {'ship_position': (0,0), 'position': (10,4)}
        forward_instruction = Instruction('F', 3)
        expected_world = twelve.main.FerryInstructions2().forward(forward_instruction, starting_world)

        self.assertEqual(expected_world, {'ship_position': (30,12), 'position': (10,4)} ) 

class FindLocationTest(unittest.TestCase):

    def test_find_location(self):
        self.assertEqual(twelve.main.find_location('twelve/example.txt'), (17, -8))

    def test_find_puzzle(self):
        self.assertEqual(twelve.main.find_location('twelve/puzzle.txt'), (17, -8))

class FerryParserTest(unittest.TestCase):

    def test_ferry_parser_example(self):
        self.assertEqual(len(twelve.main.ferry_parser('twelve/example.txt')), 5)

    def test_ferry_parser_example_returns_instructions(self):
        self.assertTrue(all( isinstance(i, Instruction) for i in twelve.main.ferry_parser('twelve/example.txt')))

    def test_ferry_parser_example_returns_instruction_arguments_are_ints(self):
        self.assertIsInstance(twelve.main.ferry_parser('twelve/example.txt')[0].argument, int)


class Findlocation2Test(unittest.TestCase):
    def test_find_location(self):
        self.assertEqual(twelve.main.find_location2('twelve/example.txt'), (214, -72))

    def test_find_puzzle(self):
        self.assertEqual(twelve.main.find_location2('twelve/puzzle.txt'), (-7074, 6266))

