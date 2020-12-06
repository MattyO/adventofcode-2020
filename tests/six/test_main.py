import unittest
import six.main

class QuestionCountTest(unittest.TestCase):

    def test_parse_groups(self):
        groups = six.main.parse('six/example.txt')

        self.assertEqual(len(groups), 5)

    def test_parse_group_lines(self):
        groups = six.main.parse('six/example.txt')

        self.assertEqual(len(groups[0]), 1)
        self.assertEqual(len(groups[1]), 3)
        self.assertEqual(len(groups[2]), 2)

    def test_question_count(self):
        lines = [
            'abcx',
            'abcy',
            'abcz',
        ]
        self.assertEqual(six.main.question_count(lines), 6) 

    def test_question_union(self):
        lines = [
            'abcx',
            'abcy',
            'abcz',
        ]
        self.assertEqual(six.main.question_union(lines), 3) 

    def test_question_union_2(self):
        lines = [
            'ab',
            'ac',
        ]
        self.assertEqual(six.main.question_union(lines), 1) 

    def test_question_exmaple_count(self):
        self.assertEqual(sum(six.main.question_count(group) for group in six.main.parse('six/example.txt')), 11)

    def test_question_exmaple_union(self):
        self.assertEqual(sum(six.main.question_union(group) for group in six.main.parse('six/example.txt')), 6)

    def test_question_count(self):
        self.assertEqual(sum(six.main.question_count(group) for group in six.main.parse('six/puzzle.txt')), 6590)

    def test_question_union(self):
        self.assertEqual(sum(six.main.question_union(group) for group in six.main.parse('six/puzzle.txt')), 3288)


