import unittest
import eight.main
import pprint

class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        self.assertEqual(len(eight.main.parse('eight/example.txt')), 9) 

    def test_parse_return_right_operand(self):
        self.assertEqual(eight.main.parse('eight/example.txt')[0].operation, 'nop') 

    def test_parse_return_right_argument(self):
        self.assertEqual(eight.main.parse('eight/example.txt')[0].argument, 0) 
        self.assertEqual(eight.main.parse('eight/example.txt')[1].argument, 1) 
        self.assertEqual(eight.main.parse('eight/example.txt')[4].argument, -3) 

    def test_comp(self):
        inst = eight.main.parse('eight/example.txt')
        c = eight.main.Comp()
        c.run(inst)
        self.assertEqual(c.accumulator, 5)

    def test_comp_has_finished_false(self):
        inst = eight.main.parse('eight/example.txt')
        c = eight.main.Comp()
        is_successful = c.run(inst)

        self.assertFalse(is_successful)

    def test_comp_has_finished_true(self):
        inst = eight.main.parse('eight/example_will_finish.txt')
        c = eight.main.Comp()
        is_successful = c.run(inst)

        self.assertTrue(is_successful)

    def test_puzzle(self):
        inst = eight.main.parse('eight/puzzle.txt')
        c = eight.main.Comp()
        c.run(inst)
        self.assertEqual(c.accumulator, 5)

    def test_fix(self):
        inst = eight.main.parse('eight/example.txt')
        c = eight.main.fix(inst)

        self.assertEqual(c.accumulator, 8)

    def test_fix_puzzle(self):
        inst = eight.main.parse('eight/puzzle.txt')
        c = eight.main.fix(inst)

        self.assertEqual(c.accumulator, 8)


