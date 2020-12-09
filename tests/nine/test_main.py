import unittest
import nine.main

class FooTest(unittest.TestCase):
    def setUp(self):
        with open('nine/example.txt') as f:
            self.example_input = list(map(lambda l: int(l.strip()), f.readlines()))

        with open('nine/puzzle.txt') as f:
            self.puzzle_input = list(map(lambda l: int(l.strip()), f.readlines()))

    def test_is_valid(self):
        self.assertTrue(nine.main.is_valid(26, range(1, 26))) 

    def test_is_valid_2(self):
        self.assertTrue(nine.main.is_valid(49, range(1, 26))) 

    def test_is_valid_false(self):
        self.assertFalse(nine.main.is_valid(100, range(1, 26))) 

    def test_is_valid_false_no_duplicate(self):
        self.assertFalse(nine.main.is_valid(50, range(1, 26))) 

    def test_is_valid_window(self):
        self.assertEqual(nine.main.is_valid_window(self.example_input, 5), 127)

    def test_is_valid_window_puzzle(self):
        self.assertEqual(nine.main.is_valid_window(self.puzzle_input , 25), 1639024365)

    def test_continuous_set(self):
        self.assertEqual(nine.main.contiguous_set(self.example_input, 127), [15,25,47,40])

    def test_continous_set_puzzle(self):
        expect_list = sorted([66794732,
                              68393057,
                              69685394,
                              69853643,
                              82799914,
                              85769459,
                              87000725,
                              87548511,
                              91579901,
                              92158454,
                              93040487,
                              99227695,
                              104998982,
                              114076413,
                              135085533,
                              138603957,
                              152407508])
        self.assertEqual(sorted(nine.main.contiguous_set(self.puzzle_input, 1639024365)), expect_list)

    def test_continous_set_puzzle_min(self):
        self.assertEqual(min(nine.main.contiguous_set(self.puzzle_input, 1639024365)), 66794732)

    def test_continous_set_puzzle_max(self):
        self.assertEqual(max(nine.main.contiguous_set(self.puzzle_input, 1639024365)), 152407508)



