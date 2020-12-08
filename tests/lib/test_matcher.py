import unittest
import lib.matcher

class MatchTest(unittest.TestCase):


    def test_match_test_string_is_true(self):
        pattern = '<test_match:string>'
        string = 'teststring'

        result = lib.matcher.match(pattern, string)

        self.assertTrue(result.is_match)

    def test_match_test_string_is_false(self):
        pattern = '<test_match:string>'
        string = 'teststring'

        result = lib.matcher.match(pattern, string)

        self.assertEqual(result.test_match, 'teststring')

    def test_match_test_int(self):
        pattern = '<test_match:int>'
        string = '1234'

        result = lib.matcher.match(pattern, string)

        self.assertTrue(result.is_match)

    def test_match_test_value(self):
        pattern = '<test_match:int>'
        string = '1234'

        result = lib.matcher.match(pattern, string)

        self.assertEqual(result.test_match, 1234)

    def test_match_success_complex_string(self):
        pattern = '1234 <test_match:string>'
        string = '1234 teststring'

        result = lib.matcher.match(pattern, string)

        self.assertTrue(result.is_match)
        self.assertEqual(result.test_match, "teststring")

    def test_match_regex(self):
        pattern = '1234 <test_match:[a-d]+>'
        string = '1234 adcbfga'


        result = lib.matcher.match(pattern, string)
        self.assertTrue(result.is_match)
        self.assertEqual(result.test_match, 'adcb')


    def test_match_puzzle_two(self):
        pattern = '<min_count:int>-<max_count:int> <letter:[a-z]>: <password:string>'
        string = '8-14 a: abdcdef'
        result = lib.matcher.match(pattern, string)
        self.assertEqual(result.min_count, 8)
        self.assertEqual(result.max_count, 14)
        self.assertEqual(result.letter, 'a')
        self.assertEqual(result.password, 'abdcdef')

