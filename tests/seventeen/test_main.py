import unittest

import mock

import seventeen.main
from seventeen.main import Point, Grid, is_active


class ParseTest(unittest.TestCase):

    def test_parse_example(self):
        grid = seventeen.main.parse('seventeen/example.txt')
        self.assertTrue(Point(0,1,0) in grid.points) 

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

    def test_next_iteration_points(self):
        self.assertEqual(len(Grid([Point(0,0,0)]).next_iteration_points()), 26)

        self.assertTrue(26 < len(Grid([Point(0,0,0), Point(0,0,1)]).next_iteration_points()) < 26*2)
        self.assertEqual(len(Grid([Point(0,0,0), Point(0,0,1)]).next_iteration_points()), 36)

        self.assertEqual(len(Grid([Point(0,0,0), Point(3,3,3)]).next_iteration_points()), 26*2 )

    def test_cycle_example_one(self):
        grid = seventeen.main.parse('seventeen/example.txt')
        grid.cycle()

        self.assertTrue(Point(0, 0, -1) in grid.points)
        self.assertTrue(Point(0, 0, 0) in grid.points)
        self.assertFalse(Point(1, 0, 0) in grid.points)

        self.assertEqual(len(grid.points), 11)

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


