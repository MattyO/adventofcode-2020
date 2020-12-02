import unittest
import two.main

class IsValidTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_valid_true(self):
        self.assertTrue(two.main.is_valid('1-3 a: abcde'))

    def test_is_valid_false(self):
        self.assertFalse(two.main.is_valid('1-3 b: cdefg'))


    def test_is_valid(self):
        items = ['1-3 a: abcde',
                 '1-3 b: cdefg',
                 '2-9 c: ccccccccc',]
        num_valid = len(list(filter(lambda i: two.main.is_valid(i), items)))
        self.assertEqual(num_valid, 2) 

    def test_is_valid_one(self):
        items = None
        with open('two/data.txt') as f:
            items = f.readlines()

        num_valid = len(list(filter(lambda i: two.main.is_valid(i), items)))
        self.assertEqual(num_valid, 517) 

    def test_is_valid_two(self):
        items = ['1-3 a: abcde',
                 '1-3 b: cdefg',
                 '2-9 c: ccccccccc',]
        num_valid = len(list(filter(lambda i: two.main.is_valid_two(i), items)))
        self.assertEqual(num_valid, 1) 

    def test_is_valid_one(self):
        items = None
        with open('two/data.txt') as f:
            items = f.readlines()

        num_valid = len(list(filter(lambda i: two.main.is_valid_two(i), items)))
        self.assertEqual(num_valid, 284) 
