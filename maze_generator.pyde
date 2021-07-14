from grid import Grid
from cell import Cell
from maze import Maze
import random as rd

WIDTH = 400
HEIGHT = 400
SCALE = 25
grid = Grid(WIDTH, HEIGHT, SCALE)
cells = []
maze = Maze(grid, cells)

def setup():
    size(WIDTH, HEIGHT)
    
def draw():
    translate(int(SCALE/2),int(SCALE/2))
    #frameRate(1)
    background(75)
    if(not maze.finished): maze.create_maze()
    else: 
        maze.made_open_and_exit()
        print("FINISH")
        noLoop()
    for cell in cells:
        cell.show()
