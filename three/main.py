class Map():
    def __init__(self, filename):
        self.trees = []
        self.height = 0
        self.width = 0

        self.load_trees(filename)

    def load_trees(self, filename):
        with open(filename) as f:
            lines = f.readlines()

        self.height = len(lines)

        for i, line in enumerate(lines):
            self.width = len(line.strip())
            for j, c in enumerate(line):
                if c == '#':
                    self.trees.append((i,j))




    def is_tree(self, position):
        if position[1] >= self.width:
           position = (position[0], position[1] % self.width )

        return position in self.trees


def points(height, slope):
    return [ (i*slope[0], i*slope[1]) for i in range(1, int(height / slope[0]))]

def trees(tree_map, slope):
    filtered_trees = list(filter(lambda p: tree_map.is_tree(p), points(tree_map.height, slope)))
    return len(filtered_trees)


