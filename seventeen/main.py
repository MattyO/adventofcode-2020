import itertools
import hashlib
import random

def is_active(point, grid):
    num_active_neightbors = len(grid.active_neighboors(point))

    if num_active_neightbors == 3:
        return True

    if point in grid.points and num_active_neightbors == 2:
        return True

    return False



class Grid():
    neighbour_offsets = [ offset for offset in itertools.product([0,1,-1], repeat=3)]

    def __init__(self, starting_points=None):
        if starting_points is None:
            starting_points = []

        self.points = starting_points

    def neighbors(self, point):
        return [Point(point.x + x, point.y + y , point.z + z) for (x,y,z) in self.neighbour_offsets if not(x == y == z == 0)]

    def next_iteration_points(self):
        next_points = set()

        for point in self.points:
            next_points |= set(self.neighbors(point))

        return next_points

    def cycle(self, count=1):
        count -= 1

        if count > 0:
            self.interation(count)


class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


    def __hash__(self):
        return int(hashlib.md5(f"{self.x}{self.y}{self.z}".encode("utf-8")).hexdigest(), 16)

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y and self.z == other_point.z

def parse(filename):
    lines = None
    points = []

    with open(filename) as f:
        lines = f.readlines()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            points.append(Point(x,y,0))

    return Grid(points)


