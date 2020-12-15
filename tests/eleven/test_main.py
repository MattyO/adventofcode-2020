import unittest

import eleven.main


class SeatTest(unittest.TestCase):

    def test_update_occupied_default(self):
        s = eleven.main.Seat(0,0)
        self.assertEqual(s.is_occupied, False)

    def test_update_occupied_more_than_4_adjacent_occupied_seats(self):
        s = eleven.main.Seat(0,0, True)
        s.update_occupied([eleven.main.Seat(0,0, True)]*4) 
        s.commit_is_occupied()
        self.assertEqual(s.is_occupied, False)

    def test_update_occupied_more_than_5_adjacent_occupied_seats(self):
        s = eleven.main.Seat(0,0, True)

        s.update_occupied([eleven.main.Seat(0,0, True)]*4, max_seats=5) 
        s.commit_is_occupied()
        self.assertEqual(s.is_occupied, True)

        s.update_occupied([eleven.main.Seat(0,0, True)]*5, max_seats=5) 
        s.commit_is_occupied()
        self.assertEqual(s.is_occupied, False)

    def test_update_occupied_no_change(self):
        s = eleven.main.Seat(0,0, True)
        self.assertEqual(s.is_occupied, True)

        s = eleven.main.Seat(0,0, False)
        s.update_occupied([eleven.main.Seat(0,0, True)]*3) 
        s.commit_is_occupied()
        self.assertEqual(s.is_occupied, False)

        s = eleven.main.Seat(0,0, True)
        s.update_occupied([eleven.main.Seat(0,0,True)]*3) 
        s.commit_is_occupied()
        self.assertEqual(s.is_occupied, True)

class GridTest(unittest.TestCase):

    def test_create_from_file(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.seats), 71) 

        self.assertEqual(len(g.seats[0]).row, 0) 
        self.assertEqual(len(g.seats[0]).column, 0) 

        self.assertEqual(len(g.seats[1]).row, 0) 
        self.assertEqual(len(g.seats[1]).column, 2) 

    def test_get_adjacent_top_left(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent(eleven.main.Seat(0,0))), 2)

    def test_get_adjacent_0_3(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent(eleven.main.Seat(0,2))), 4)

    def test_get_adjacent_1_2(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent(eleven.main.Seat(1,2))), 5)

    def test_get_adjacent2_0_0(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent2(eleven.main.Seat(0,0))), 3 )

    def test_get_adjacent2_0_1(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent2(eleven.main.Seat(0,1))), 9)

    def test_get_adjacent2_1_0(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        self.assertEqual(len(g.get_adjacent2(eleven.main.Seat(1,0))), 9)

    def test_get_adjacent2_return_eight_example(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/adjacent_example.txt')
        self.assertEqual(len(g.get_adjacent2(eleven.main.Seat(4,3))), 8)

    def test_get_adjacent2_return_one_example(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/adjacent_example2.txt')
        adjacents = g.get_adjacent2(eleven.main.Seat(1,1))
        self.assertEqual(len(adjacents), 1)
        self.assertEqual(adjacents[0].row, 1)
        self.assertEqual(adjacents[0].column, 3)
        self.assertEqual(adjacents[0].is_occupied, False)

    def test_get_adjacent2_return_zero_example(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/adjacent_example3.txt')
        adjacents = g.get_adjacent2(eleven.main.Seat(3,3))
        self.assertEqual(len(adjacents), 0)

    def test_round_one_fills_all_seats(self):
        g = eleven.main.Grid()
        g.create_from_file('eleven/example.txt')
        g.round()
        self.assertEqual(len(g.seats), g.num_occupied())


    def test_round_example_stabalizes_at_5_rounds(self):
        g= eleven.main.Grid()
        g.create_from_file('eleven/example.txt')

        counter = 0
        old_num = None 
        new_num = g.num_occupied()

        while old_num != new_num:
            old_num = g.num_occupied()
            g.round()
            new_num = g.num_occupied()
            counter += 1

        self.assertEqual(counter, 6)
        self.assertEqual(g.num_occupied(), 37)


    def test_round_puzzle_stabalizes(self):
        g= eleven.main.Grid()
        g.create_from_file('eleven/puzzle.txt')

        counter = 0
        old_num = None 
        new_num = g.num_occupied()

        while old_num != new_num:
            old_num = g.num_occupied()
            g.round()
            new_num = g.num_occupied()
            counter += 1

        self.assertEqual(counter, 78)
        self.assertEqual(g.num_occupied(), 37)


    def test_round2_example_stabalizes(self):
        g= eleven.main.Grid()
        g.create_from_file('eleven/example.txt')

        counter = 0
        old_num = None 
        new_num = g.num_occupied()

        while old_num != new_num:
            old_num = g.num_occupied()
            g.round2()
            #g.print()
            #print("\n")

            new_num = g.num_occupied()
            counter += 1

        self.assertEqual(g.num_occupied(), 26)
        self.assertEqual(counter, 7)

    def test_round2_puzzle_stabalizes(self):
        g= eleven.main.Grid()
        g.create_from_file('eleven/puzzle.txt')

        counter = 0
        old_num = None 
        new_num = g.num_occupied()

        while old_num != new_num:
            old_num = g.num_occupied()
            g.round2()

            new_num = g.num_occupied()
            counter += 1

        self.assertEqual(g.num_occupied(), 2197)
        self.assertEqual(counter, 7)

class CollinearTest(unittest.TestCase):

    def test_collinear_true(self):
        self.assertTrue(eleven.main.is_collinear(eleven.main.Seat(0,0), 
                                              eleven.main.Seat(1,1),
                                              eleven.main.Seat(1,1)))

    def test_collinear_false(self):
        self.assertFalse(eleven.main.is_collinear(eleven.main.Seat(0,0), 
                                              eleven.main.Seat(1,1),
                                              eleven.main.Seat(1,2)))

class QuadrantTest(unittest.TestCase):

    def test_quadrant_1(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(3,2)),
                         (1,1))

    def test_quadrant_2(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(3, -2)),
                         (-1,1))

    def test_quadrant_3(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(-3,-2)),
                         (-1,-1))

    def test_quadrant_4(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(-3,2)),
                         (1,-1))

    def test_quadrant_top(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(3,0)),
                         (0,1))

    def test_quadrant_bottom(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(-3,0)),
                         (0,-1))

    def test_quadrant_left(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(0,-2)),
                         (-1, 0))

    def test_quadrant_right(self):
        self.assertEqual(eleven.main.quadrant(eleven.main.Seat(0,0),eleven.main.Seat(0,2)),
                         (1, 0))

