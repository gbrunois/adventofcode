def parse_lines():
    with open("input.txt") as f:
        return [(line.strip()) for line in f.readlines()]

class Grid:
    def __init__(self, lines):
        self.world = {}
        self.x_dim = (0,len(lines[0]))
        self.y_dim = (0,len(lines))
        self.z_dim = (0,1)
        self.w_dim = (0,1)

        for i in range(0, len(lines[0])):
            for row in range(0, len(lines)):
                if lines[i][row] == "#":
                    self[i, row, 0, 0] = True

    def get_sum_active_neighbours(self, i, j, k, l):
            return sum(((x, y, z, w) in self.world) 
            for x in range(i-1, i+2)
            for y in range(j-1, j+2)
            for z in range(k-1, k+2)
            for w in range(l-1, l+2)
            if (x, y, z, w) != (i, j, k, l))

    def run(self):
        leaving = []
        activate = []
        # expand the world
        self.x_dim = (self.x_dim[0]-1, self.x_dim[1]+1)
        self.y_dim = (self.y_dim[0]-1, self.y_dim[1]+1)
        self.z_dim = (self.z_dim[0]-1, self.z_dim[1]+1)
        self.w_dim = (self.w_dim[0]-1, self.w_dim[1]+1)
        
        for i in range(*self.x_dim):
            for j in range(*self.y_dim):
                for k in range(*self.z_dim):
                    for l in range(*self.w_dim):
                        sum_active_neighbours = self.get_sum_active_neighbours(i, j, k, l)
                    
                        if self[i, j, k, l] and sum_active_neighbours != 2 and sum_active_neighbours != 3:
                            leaving.append((i, j, k, l))
                        if self[i, j, k, l] == False and sum_active_neighbours == 3:
                            activate.append((i, j, k, l))

        
        for (i, j, k, l) in leaving:
            self.world.pop((i, j, k, l))
        for (i, j, k, l) in activate:
            self[i, j, k, l] = True

        print(len(self.world.keys()))

    def __getitem__(self, coord):
        return self.world[coord] if coord in self.world else False

    def __setitem__(self, coord, value):
        x, y, z, w = coord
        self.world[(x, y, z, w)] = value



grid = Grid(parse_lines())
for i in range(0,6):
    grid.run()
