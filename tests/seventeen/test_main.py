import unittest

import mock

import seventeen.main
from seventeen.main import Point, Grid, is_active


class ParseTest(unittest.TestCase):
    def setUp(self):
        self.grid = seventeen.main.parse('seventeen/example.txt')

    def test_parse_example(self):
        self.assertTrue(Point(1,0,0) in self.grid.points) 
        self.assertTrue(Point(2,1,0) in self.grid.points) 

    def test_doesnt_include_non_hash_characters(self):
        self.assertFalse(Point(0,0,0) in self.grid.points) 

    def test_example_count(self):
        self.assertEqual(len(self.grid.points), 5)


class PointTest(unittest.TestCase):

    def test___eq__(self):
        self.assertEqual(Point(0,1,0), Point(0,1,0))
        self.assertNotEqual(Point(1,1,0), Point(0,1,0))

    def test_hash(self):
        t = {}
        t[Point(0,0,0)] = 'test'
        t[Point(0,0,0)] = 'test2'

        self.assertEqual(len(t.items()),1) 



class GridTest(unittest.TestCase):

    def test_neighbors(self):
        self.assertEqual(len(Grid([]).neighbors(Point(1,1,1))), 26) 
        self.assertEqual(len(Grid([]).neighbors(Point(3,3,3))), 26) 
        self.assertTrue(Point(2,2,2,) in Grid([]).neighbors(Point(3,3,3)))
        self.assertFalse(Point(0,2,2) in Grid([]).neighbors(Point(3,3,3)))

    def test_next_iteration_points(self):
        self.assertEqual(len(Grid([Point(0,0,0)]).next_iteration_points()), 26)

        self.assertTrue(26 < len(Grid([Point(0,0,0), Point(0,0,1)]).next_iteration_points()) < 26*2)
        self.assertEqual(len(Grid([Point(0,0,0), Point(0,0,1)]).next_iteration_points()), 36)

        self.assertEqual(len(Grid([Point(0,0,0), Point(3,3,3)]).next_iteration_points()), 26*2 )

    def test_cycle_example_one(self):
        grid = seventeen.main.parse('seventeen/example.txt')
        self.assertEqual(len(grid.points), 5)

        grid.cycle()

        print(len(grid.points))
        self.assertTrue(Point(0, 0, -1) in grid.points)
        self.assertTrue(Point(0, 0, 0) in grid.points)
        self.assertFalse(Point(1, 0, 0) in grid.points)

        self.assertEqual(len(grid.points), 11)

    def test_cycle_example_six(self):
        grid = seventeen.main.parse('seventeen/example.txt')
        grid.cycle(6)
        self.assertEqual(len(grid.points), 112)

    def test_active_neighboors(self):
        points = [Point(0,0,0), Point(0,0,1), Point(1,1,1), Point(3,0,1)]
        grid =Grid(points)

        self.assertEqual(len(grid.active_neighboors(Point(0,0,0,))), 2)

    def test_active_neighboors_example(self):
        grid = seventeen.main.parse('seventeen/example.txt')
        neighbors = grid.active_neighboors(Point(0,0,-1))

        self.assertEqual(len(neighbors), 3)


class IsActiveTest(unittest.TestCase):

    def test_is_active_3(self):
        grid_mock = mock.Mock()
        grid_mock.active_neighboors.return_value = [Point(0,0,0), Point(1,0,1), Point(1,0,0)]
        self.assertTrue(is_active(Point(0,1,0), grid_mock)) 

    def test_is_active_2(self):
        points = [Point(0,0,0), Point(1,0,1), Point(1,0,0)]
        grid_mock = mock.Mock(points=points)
        grid_mock.active_neighboors.return_value = [Point(1,0,1), Point(1,0,0)]

        self.assertTrue(is_active(Point(0,0,0), grid_mock)) 

    def test_is_active_2_return_false_if_point_isnt_active(self):
        points = [Point(0,1,0), Point(1,0,1), Point(1,0,0)]
        grid_mock = mock.Mock(points=points)
        grid_mock.active_neighboors.return_value = [Point(1,0,1), Point(1,0,0)]

        self.assertFalse(is_active(Point(0,0,0), grid_mock)) 


    def test_is_active_4_return_false(self):
        points = [Point(0,1,0), Point(1,0,1), Point(1,0,0), Point(1,1,1)]
        grid_mock = mock.Mock(points=points)
        grid_mock.active_neighboors.return_value = [Point(1,0,1), Point(1,0,0)]

        self.assertFalse(is_active(Point(0,0,0), grid_mock)) 


