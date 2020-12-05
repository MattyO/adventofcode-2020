import unittest
import five.main

class SeatIdTest(unittest.TestCase):

    def test_seat_id(self):
        self.assertEqual(five.main.seat_id("FBFBBFFRLR"), (44, 5, 357 ))

    def test_seat_id_2(self):
        self.assertEqual(five.main.seat_id("BFFFBBFRRR"), (70, 7, 567 ))

    def test_seat_id_3(self):
        self.assertEqual(five.main.seat_id("FFFBBBFRRR"), (14, 7, 119 ))

    def test_seat_id_4(self):
        self.assertEqual(five.main.seat_id("BBFFBBFRLL"), (102, 4, 820))

    def test_seat_id_highest_seat_id(self):
        with open("five/input.txt") as f:
            lines = f.readlines()

        self.assertEqual(max(map(lambda l: five.main.seat_id(l.strip())[-1], lines)), 926)

    def test_seat_id_missing_seats(self):
        with open("five/input.txt") as f:
            lines = f.readlines()

        seats = list(map(lambda l: five.main.seat_id(l.strip()), lines))
        ids = list(map(lambda s: s[-1], seats))
        missing = sorted([ i for i in range(80, 927) if i not in ids ])

        self.assertEqual(missing, [657] )

