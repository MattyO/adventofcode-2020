import unittest
import three.main

class MapTest(unittest.TestCase):
    def setUp(self):
        self.example_map = three.main.Map("three/data_example.txt")

    def test_map(self):
        self.assertIsInstance(three.main.Map("three/data_example.txt"), three.main.Map)

    def test_map_trees(self):
        m = three.main.Map("three/data_example.txt")
        self.assertEqual(m.trees[0], (0,2))
        self.assertEqual(m.trees[1], (0,3))
        self.assertEqual(m.trees[2], (1,0))

    def test_map_check_tree(self):
        m = three.main.Map("three/data_example.txt")
        self.assertFalse(m.is_tree((0,0)))
        self.assertTrue(m.is_tree((0,2)))
        self.assertTrue(m.is_tree((0,3)))

    def test_map_check_tree_off_edge(self):
        m = three.main.Map("three/data_example.txt")
        self.assertFalse(m.is_tree((0,11)))
        self.assertTrue(m.is_tree((0,13)))
        self.assertTrue(m.is_tree((0,14)))
        #self.assertFalse(m.is_tree((4,12)))
        self.assertTrue(m.is_tree((4,12)))
        self.assertTrue(m.is_tree((5,15)))
        self.assertTrue(m.is_tree((7,21)))
        #self.assertTrue(m.is_tree((9,27)))

    def test_map_height(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(m.height, 11)

    def test_points(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(three.main.points(m.height, (1,3))[0], (1,3))

    def test_points_is_the_right_length(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(len(three.main.points(m.height, (1,3))), 10) 

    def test_points_last_point(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(three.main.points(m.height, (1,3))[-1], (10,30))

    def test_trees(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(three.main.trees(m, (1, 3)),  7) 

    def test_trees_one(self):
        m = three.main.Map("three/data_one.txt")
        m.trees
        self.assertEqual(three.main.trees(m, (1, 3)),  292) 

    def test_trees_two_example(self):
        m = three.main.Map("three/data_example.txt")
        m.trees
        self.assertEqual(three.main.trees(m, (1, 1)),  2) 
        self.assertEqual(three.main.trees(m, (1, 3)),  7) 
        self.assertEqual(three.main.trees(m, (1, 5)),  3) 
        self.assertEqual(three.main.trees(m, (1, 7)),  4) 
        self.assertEqual(three.main.trees(m, (2, 1)),  2) 

    def test_trees_two_puzzel(self):
        m = three.main.Map("three/data_one.txt")
        self.assertEqual(three.main.trees(m, (1, 1)),  81) 
        self.assertEqual(three.main.trees(m, (1, 3)),  292) 
        self.assertEqual(three.main.trees(m, (1, 5)),  89) 
        self.assertEqual(three.main.trees(m, (1, 7)),  101) 
        self.assertEqual(three.main.trees(m, (2, 1)),  44) 

