import unittest
import one.main

class OneTest(unittest.TestCase):
    def test_two_numbers(self):
        possible_numbers = [1721,
        979,
        366,
        299,
        675,
        1456]

        result = one.main.two_numbers(possible_numbers)

        self.assertEqual(result, (1721, 299)) 

    def test_two_numbers_two(self):
        possible_numbers = None
        with open('one/data.txt') as f:
            possible_numbers = [ int(line) for line in f.readlines() ]

        result = one.main.two_numbers(possible_numbers)
        self.assertEqual(result, (1301, 719)) 

    def test_three_numbers(self):
        possible_numbers = [1721,
        979,
        366,
        299,
        675,
        1456]

        result = one.main.three_numbers(possible_numbers)

        self.assertEqual(result, (979, 366, 675)) 

    def test_three_numbers_two(self):
        possible_numbers = None
        with open('one/data.txt') as f:
            possible_numbers = [ int(line) for line in f.readlines() ]

        result = one.main.three_numbers(possible_numbers)

        self.assertEqual(result, (889, 1079, 52)) 

