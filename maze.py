from cell import Cell
import random as rd

class Maze:
    def __init__(self, grid, cells):
        self.grid = grid
        self.cells = cells
        self.i = -1
        self.finished = False
        self.max_index = self.grid.grid.index(max(self.grid.grid))
        self.current_cell = Cell(0,0,grid)
        self.current_cell.visited = True
        self.cells.append(self.current_cell)

    def get_cell_by_id(self,new_cell):
        i,j = new_cell
        for cell in self.cells:
            if(cell.i == i and cell.j == j): return self.cells.index(cell)
        return False
    
    def get_move(self,current_cell, old_cell):
        direction = [ current_cell.i - old_cell.i, current_cell.j - old_cell.j]
        index_actived_bit = int(not direction.index(0))
        if(index_actived_bit == 0):
            if(direction[index_actived_bit] == 1):
                old_cell.wall[2] = False
                current_cell.wall[0] = False
            else:
                old_cell.wall[0] = False
                current_cell.wall[2] = False
        else:
            if(direction[index_actived_bit] == -1):
                old_cell.wall[3] = False
                current_cell.wall[1] = False
            else:
                old_cell.wall[1] = False
                current_cell.wall[3] = False
    
    def possible_moves(self, cell):
        moves = [[0, 1],[1, 0], [-1, 0], [0, -1]]
        move_valid = False
        while len(moves) > 0:
            move_x, move_y = rd.sample(moves, 1)[0]
            moves.remove([move_x, move_y])    
            new_cell = [cell.i + move_x, cell.j + move_y]
            was_visited = type(self.get_cell_by_id(new_cell)) == int
            if(was_visited or (self.max_index in new_cell) or (-1 in new_cell) ): continue
            else:
                move_valid = True
                break
        return new_cell if move_valid else False
    
    def create_maze(self):
        started = self.current_cell
        started.visited = True
        new_move = self.possible_moves(started)
        if(new_move): ### new move
            i,j = new_move
            new_cell = Cell(i,j,self.grid)
            valid_move = self.get_move(new_cell, started)
            new_cell.visited = True
            self.cells.append(new_cell)
            self.current_cell = new_cell
            self.i = -1
            
        elif(self.max_index ** 2 > (len(self.cells))):
            old_cell = self.cells[self.i]
            self.current_cell = old_cell
            self.i -= 1
            return
        else:
            self.finished = True
            
        self.current_cell.draw_rect()
    
    def made_open_and_exit(self):
        front_door_x, front_door_y = 0,0
        back_door_x, back_door_y = self.max_index - 1, self.max_index - 1
    
        front_door_id = self.get_cell_by_id([front_door_x, front_door_y])
        back_door_id = self.get_cell_by_id([back_door_x, back_door_y])
        
        self.cells[front_door_id].wall[0] = False

        self.cells[back_door_id].wall[2] = False        
