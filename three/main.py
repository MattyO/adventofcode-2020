class Map():
    def __init__(self, filename):
        self.filename = filename
        self._trees = None
        self.width = None
        self.height = None

    @property
    def trees(self):
        if self._trees is None:
            self._trees = []
            with open(self.filename) as f:
                lines = f.readlines()

            self.height = len(lines)

            for i, line in enumerate(lines):
                self.width = len(line.strip())
                for j, c in enumerate(line):
                    if c == '#':
                        self._trees.append((i,j))

        return self._trees

    def is_tree(self, position):
        self.trees

        if position[1] >= self.width:
           #print(position[1])
           position = (position[0], position[1] % self.width )
        #print(self.width)
        #print(position)

        return position in self.trees


def points(height, slope):
    return [ (i*slope[0], i*slope[1]) for i in range(1, int(height / slope[0]))]

def trees(tree_map, slope):
    #print(points(tree_map.height, slope))
    filtered_trees = list(filter(lambda p: tree_map.is_tree(p), points(tree_map.height, slope)))
    #print(filtered_trees)
    return len(filtered_trees)


