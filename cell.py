class Cell:
    def __init__(self, i, j, grid):
        self.i = i
        self.j = j
        self.SCALE = grid.SCALE
        self.visited = False
        self.wall = [True, True, True, True]
        self.grid = grid.grid
        
    def show(self):
        x1,y1 = self.grid[self.i][self.j]
        x2,y2 = x1,y1
        noStroke()
        fill(255)
        strokeWeight(1)
        stroke(175.5,175,175.5)
        index_wall = 0 # 0: wall right; 1: wall down, 2: wall left, 3: wall up
        for w in self.wall:
            
            if(index_wall == 0):
                y2 += self.SCALE    
            if(index_wall == 1):
                x2 += self.SCALE
            if(index_wall == 2):
                y2 -= self.SCALE
            if(index_wall == 3):
                x2 -= self.SCALE 
            if(w):
                line(x1,y1, x2, y2)   
            x1,y1 = x2,y2
            index_wall += 1
            
    def draw_rect(self):
        
        noStroke()
        fill(255,0,0)
        rect(self.grid[self.i][self.j][0], self.grid[self.i][self.j][1], self.SCALE, self.SCALE)
