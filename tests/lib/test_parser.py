import unittest
import lib.parser

from pprint import pprint

class FileGroupedByBlankeLinesTest(unittest.TestCase):

    def test_file_grouped_by_blanke_lines(self):
        result = lib.parser.file_grouped_by_blanke_lines("four/data_example.txt")

        self.assertEqual(len(result),4) 

    def test_file_grouped_by_blanke_lines_check_group_lengths(self):
        result = lib.parser.file_grouped_by_blanke_lines("four/data_example.txt")

        pprint(result)
        self.assertEqual(len(result[0]), 2)
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(len(result[2]), 4)

    def test_file_grouped_by_blanke_lines_check_group_lengths(self):
        result = lib.parser.file_grouped_by_blanke_lines("four/data_example.txt")

        self.assertEqual(len(result[0]), 2)
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(len(result[2]), 4)

    def test_file_grouped_by_blanke_lines_check_group_lengths(self):
        pass
        #TODO: make me


