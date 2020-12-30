import unittest
import fifteen.main

class GameLIstTest(unittest.TestCase):

    def test_item_at_example_4(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 4),
            0
        ) 

    def test_item_at_example_5(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 5),
            3
        ) 

    def test_item_at_example_6(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 6),
            3
        ) 

    def test_item_at_example_7(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 7),
            1
        ) 

    def test_item_at_example_8(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 8),
            0
        ) 
    def test_item_at_example_9(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 9),
            4
        ) 
    def test_item_at_example_10(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 10),
            0
        )

    def test_item_at_example_2020(self):
        self.assertEqual(
            fifteen.main.item_at([0,3,6], 2020),
            436
        ) 

    def test_puzzle(self):
        self.assertEqual(
            fifteen.main.item_at([0,5,4,1,10,14,7], 2020),
            203 
        ) 

    def test_puzzle_part2(self):
        self.assertEqual(
            fifteen.main.item_at([0,5,4,1,10,14,7], 30000000),
            9007186
        )

