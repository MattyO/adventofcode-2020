import unittest
import thirteen.main

class FindBusTest(unittest.TestCase):

    def parse_file(self, filename):
        lines = None
        with open(filename) as f:
            lines = f.readlines()
        start_point = int(lines[0])
        bus_ids = [ None if i =='x' else  int(i) for i in lines[1].strip().split(',') ]

        return ( start_point, bus_ids)

    def test_puzzle_input(self):
        puzzle_input = self.parse_file('thirteen/example.txt')
        self.assertEqual(
            puzzle_input, 
            ((939), [7, 13, None, None, 59, None, 31, 19])
        )
    def test_find_departure_example(self):
        puzzle_input = self.parse_file('thirteen/example.txt')
        starting_point, bus_ids = puzzle_input

        self.assertEqual(
            thirteen.main.find_departure(starting_point, bus_ids),
            (944, 59)
        )

    def test_find_departure_puzzle(self):
        puzzle_input = self.parse_file('thirteen/puzzle.txt')
        starting_point, bus_ids = puzzle_input

        self.assertEqual(
            thirteen.main.find_departure(starting_point, bus_ids),
            (1000059, 17)
        )




class FindCombinationTest(unittest.TestCase):
    def parse_file(self, filename):
        lines = None
        with open(filename) as f:
            lines = f.readlines()
        start_point = int(lines[0])
        bus_ids = [ (i, int(bus_id)) for i, bus_id in enumerate(lines[1].strip().split(',')) if bus_id != 'x' ]

        return bus_ids

    def test_find_combination_smallest(self):
        small_input = [(0, 17), (2, 13)]

        self.assertEqual(
            thirteen.main.find_combination(small_input),
           102
        )
    def test_find_combination_small(self):
        small_input = [(0, 17), (2, 13), (3, 19)]

        self.assertEqual(
            thirteen.main.find_combination(small_input),
            3417
        )

    def test_find_combination_2(self):
        small_input = [(0, 67), (1, 7), (2, 59), (3, 61)]
        self.assertEqual(
            thirteen.main.find_combination(small_input),
            754018
        )

    def test_find_combination_3(self):
        small_input = [(0, 67), (2, 7), (3, 59), (4, 61)]
        self.assertEqual(
            thirteen.main.find_combination(small_input),
            779210
        )

    def test_find_combination_4(self):
        small_input = [(0, 67), (1, 7), (3, 59), (4, 61)]
        self.assertEqual(
            thirteen.main.find_combination(small_input),
            1261476
        )
    def test_find_combination_4(self):
        small_input = [(0, 1789), (1, 37), (2, 47), (3, 1889)]

        self.assertEqual(
            thirteen.main.find_combination(small_input),
            1202161486
        )


    def test_find_combination_puzzle(self):
        puzzle_input = self.parse_file('thirteen/puzzle.txt')

        self.assertEqual(
            thirteen.main.find_combination(puzzle_input),
            1106724616194525
        )
