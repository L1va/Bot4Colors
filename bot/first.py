
from collections import Counter
games = dict()

class Game:
    def __init__(self, board):
        print(board)
        #self.count = board["figures_count"]
        self.cells = dict()
        #self.not_used = dict()     
        cells = board["cells"]   
        for i in range (len(cells)):
            row = cells[i]
            for j in range(len(row)):
                cur_id = row[j]                
                if cur_id in self.cells:
                    cur_cell = self.cells[cur_id]
                else:
                    cur_cell = Cell(cur_id,self)
                    self.cells[cur_id] = cur_cell
                    #self.not_used[cur_id] = True
                if i!=0:
                    up_id = cells[i-1][j]
                    if up_id!=cur_id:
                        cur_cell.add(up_id)
                        up_c = self.cells[up_id]
                        up_c.add(cur_id)
                if j!=0:
                    left_id = cells[i][j-1]
                    if left_id!=cur_id:
                        cur_cell.add(left_id)
                        left_c = self.cells[left_id]
                        left_c.add(cur_id)


class Cell:
    def __init__(self, id, game):
        self.game = game
        self.id = id
        self.neigh = dict()
        self.color = -1

    def add(self, id):
        self.neigh[id] = True

    def can_color(self, color):
        for id,v in self.neigh.items():
            c = self.game.cells[id]
            if c.color == color:
                return False
        return True

def max_count(id, color):
    game = games[id]
    for id,c in game.cells.items():
        if c.color==-1 and c.can_color(color):
            c.color = color
            return id
    
def enemy_step(id, fig, color):
    game = games[id]
    game.cells[fig].color = color
  
