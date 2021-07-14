class Grid:
    def __init__(self, WIDTH, HEIGHT, SCALE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCALE = SCALE
        self.grid = []
        self.create_grid()
        
    def create_grid(self):
        col = floor(self.WIDTH/self.SCALE)
        row = floor(self.HEIGHT/self.SCALE)
        for x in range(col):
            self.grid.append([])
            for y in range(row):
                self.grid[-1].append([self.SCALE*x, self.SCALE*y])
