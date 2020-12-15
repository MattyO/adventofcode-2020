import itertools
import copy
import collections
import math
from pprint import pprint

class Seat():
    def __init__(self, row, column, is_occupied=False):
        self.is_occupied = is_occupied
        self.row = row
        self.column= column
        self.temp_is_occupied = None


    def __repr__(self):
        return f"Seat({self.row}, {self.column} | {self.is_occupied})"

    def commit_is_occupied(self):
        self.is_occupied = self.temp_is_occupied
        self.temp_is_occupied = None

    def update_occupied(self, seats, max_seats=4):
        num_adjacent_occupied_seats = len( [s for s in seats if s.is_occupied ])

        self.temp_is_occupied = self.is_occupied

        if num_adjacent_occupied_seats == 0:
            self.temp_is_occupied = True

        if num_adjacent_occupied_seats >= max_seats:
            self.temp_is_occupied = False


def is_collinear(seat1, seat2, seat3):
    return ((seat2.column - seat1.column) * (seat3.row - seat2.row)) == ((seat3.column - seat2.column)*(seat2.row - seat1.row))

def distance(r1, r2, c1, c2):
    return math.sqrt(((r1-r2)**2) + ((c1-c2)**2))

def quadrant(s1, s2):
    if s2.column == s1.column:
        col = 0
    else:
        col = int((s2.column - s1.column) / math.fabs( s2.column - s1.column))

    if s2.row == s1.row:
        row = 0
    else:
        row = int((s2.row - s1.row) / math.fabs( s2.row - s1.row))

    return (col,row)


class Grid():
    def __init__(self):
        self.seats_hash = collections.defaultdict(lambda: collections.defaultdict(lambda: None))
        self.seats = []
        self.num_rows = None
        self.num_columns= None


    def create_from_file(self, filename):
        self.seats.clear()
        lines = None
        with open(filename) as f:
            lines = f.readlines()

        for row, line in enumerate(lines):
            self.num_rows = len(lines)
            for column, c in enumerate(line):
                self.num_columns = len(line) -1
                if c == 'L' or c == '#':
                    is_occupied = False
                    if c == '#':
                        is_occupied =True

                    new_seat = Seat(row, column,is_occupied)
                    self.seats_hash[row][column] = new_seat
                    self.seats.append(new_seat)


    def print(self):
        for r in range(0, self.num_rows):
            temp_line = ""
            for c in range(0, self.num_columns):
                s = self.get_seat(r,c)
                if s is None: 
                    temp_line += '.'
                    continue
                if s.is_occupied:
                    temp_line += "#"
                else: 
                    temp_line += "L"

            print(temp_line)

    def round(self):
        for s in self.seats:
            s.update_occupied(self.get_adjacent(s))

        for s in self.seats:
            s.commit_is_occupied()

    def round2(self):
        for s in self.seats:

            s.update_occupied(self.get_adjacent2(s), max_seats=5)

        for s in self.seats:
            s.commit_is_occupied()

    def num_occupied(self):
        return len([s for s in self.seats if s.is_occupied])

    def get_seat(self, row, column):
        return self.seats_hash[row][column]

    def get_adjacent2(self, seat):

        adjacent_seats = []
        possible_positions = []
        max_offset_row = max(int(math.fabs(seat.row - self.num_rows)), int(math.fabs(0-seat.row)))
        max_offset_col = max(int(math.fabs(seat.column - self.num_columns)), int(math.fabs(0-seat.column)))
        max_offset = max(max_offset_row, max_offset_col)
        for i in range(1, max_offset + 1):
            temp_possible_positions = []
            offsets = list(set(list(itertools.permutations([0] + ([i]*2) + ([-i]*2), 2))))
            temp_possible_positions = [ (row_offset + seat.row, column_offset + seat.column) for row_offset, column_offset in offsets ]
            possible_positions += [ (row, column) for row, column in temp_possible_positions if 0 <= row <= self.num_rows and 0 <= column <= self.num_columns]



        possible_position_groups = []
        while len(possible_positions) > 0: 
            check_against = possible_positions[0]
            new_group = list(filter(lambda p:  is_collinear( seat, Seat(*check_against), Seat(*p)), possible_positions))
            possible_position_groups.append(new_group)
            for p in new_group:
                possible_positions.remove(p)


        new_possble_positions = []
        for group in possible_position_groups:
            group_with_quad = [ (quadrant(seat, Seat(*s)), s) for s in group]
            group_with_quad = sorted(group_with_quad, key=lambda s: s[0])

            quad_groups = itertools.groupby(group_with_quad, key=lambda s: s[0])

            for k, g in quad_groups:
                new_possble_positions.append([gs[1] for gs in g])

        possible_position_groups = new_possble_positions


        for positions in possible_position_groups:
            sorted_positions = sorted(positions, key=lambda p: distance(seat.row, p[0], seat.column, p[1]), )
            sorted_seats = [ self.get_seat(*p) for p in sorted_positions ]
            closest_position_in_group = next(filter(lambda s: s is not None, sorted_seats), None)
            if closest_position_in_group is not None:
                adjacent_seats.append(closest_position_in_group)
                continue


        return adjacent_seats






        #returned_seats = []

        #positions_to_check = []
        #for row in range(0, self.num_rows):
        #    if row == seat.row:
        #        for column in range(0, self.num_columns):
        #            if column < seat.column:
        #                group = 'left'
        #            else:
        #                group = 'right'
        #            if column != seat.column:
        #                positions_to_check.append((group, row, column))
        #    else:
        #        if row < seat.row:
        #            group = 'top'
        #        else:
        #            group = 'bottom'
        #        positions_to_check.append((group, row,seat.column))
        #        positions_to_check.append((f'{(row-seat.row)/(row-seat.row)}',row,(row - seat.row)))
        #        positions_to_check.append((f'{(row-seat.row)/(seat.row -row)}', row,(seat.row - row)))


        #grouped_seats = itertools.groupby(sorted(positions_to_check, key=lambda s: s[0]), key=lambda s: s[0])
        #for slope, group in grouped_seats:
        #    sorted_group = list(sorted(group, key=lambda s: distance(seat.row, s[1], seat.column, s[2])))
        #    #print(sorted_group)
        #    for s in sorted_group:
        #        if self.get_seat(s[1], s[2]) is not None:
        #            #print("found seat {row}, {column}")
        #            returned_seats.append(self.get_seat(s[1], s[2]))
        #            break;

        #return returned_seats


    def get_adjacent(self, seat):
        offsets = list(set(list(itertools.permutations([0,1,1,-1,-1], 2))))
        positions_to_check = [ (seat.row + row, seat.column + column) for row, column in offsets ]

        temp = list(filter(lambda s: s is not None, [ self.get_seat(row, column) for row, column in positions_to_check ]))
        return temp
