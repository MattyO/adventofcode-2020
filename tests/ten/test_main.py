import unittest
import ten.main

class VoltageDifferenceTest(unittest.TestCase):

    def input(self, filename):
        lines = None
        with open(filename) as f:
            lines = map(lambda l: int(l), f.readlines())

        return lines


    def test_voltage_difference_small_example(self):
        self.assertEqual(ten.main.voltage_difference(self.input('ten/small_example.txt')), 22)

    def test_voltage_difference_example(self):
        self.assertEqual(ten.main.voltage_difference(self.input('ten/example.txt')), 52)

    def test_voltage_difference_puzzle(self):
        self.assertEqual(ten.main.voltage_difference(self.input('ten/puzzle.txt')), 186)

    def test_aragements_small(self):
        self.assertEqual(ten.main.arangements(self.input('ten/small_example.txt')), 8)

    def test_aragements_example(self):
        self.assertEqual(ten.main.arangements(self.input('ten/example.txt')), 19208)

    def test_aragements_puzzle(self):
        self.assertEqual(ten.main.arangements(self.input('ten/puzzle.txt')), 518344341716992)

