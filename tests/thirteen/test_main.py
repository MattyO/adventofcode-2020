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
            944
        )

    def test_find_departure_puzzle(self):
        puzzle_input = self.parse_file('thirteen/puzzle.txt')
        starting_point, bus_ids = puzzle_input
        print(starting_point)

        self.assertEqual(
            thirteen.main.find_departure(starting_point, bus_ids),
            (1000059, 17)
        )




