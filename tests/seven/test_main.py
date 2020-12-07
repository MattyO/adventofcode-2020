import unittest
import seven.main
from pprint import pprint

class BagTest(unittest.TestCase):


    def test_parse(self):
        bag_nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(len(bag_nodes), 9)

    def test_parse_parent(self):
        bag_nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(bag_nodes[0][0], 'light red')

    def test_parse_children(self):
        bag_nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(len(bag_nodes[0][1]), 2)

    def test_parse_children_none(self):
        bag_nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(len(bag_nodes[-1][1]), 0)

    def test_get_child_name(self):
        node = ('light red', [('bright white', '1'), ('muted yellow', '2')])
        self.assertEqual(seven.main.get_child_names(node), ['bright white', 'muted yellow'])

    def test_get_node_with_children(self):
        bag_nodes = seven.main.parse('seven/example.txt')
        nodes = seven.main.get_nodes_with_children(bag_nodes, 'shiny gold')
        self.assertEqual(len(nodes), 2)

        self.assertEqual(list(map(lambda n: n[0], nodes)), ['bright white', 'muted yellow'])

    def test_get_parent(self):
        nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(len(set(seven.main.get_parents(nodes, 'shiny gold'))), 4)

    def test_get_parent_puzzel(self):
        nodes = seven.main.parse('seven/puzzle.txt')
        self.assertEqual(len(set(seven.main.get_parents(nodes, 'shiny gold'))), 233)

    def test_count_children(self):
        nodes = seven.main.parse('seven/example.txt')
        self.assertEqual(seven.main.count_children(nodes, 'shiny gold'), 32)

    def test_count_children_example_2(self):
        nodes = seven.main.parse('seven/example2.txt')
        self.assertEqual(seven.main.count_children(nodes, 'shiny gold'), 126)

    def test_get_node(self):
        nodes = seven.main.parse('seven/puzzle.txt')
        self.assertEqual(seven.main.count_children(nodes, 'shiny gold'), 421550)

