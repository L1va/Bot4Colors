games = dict()


class Game:
    def __init__(self, board):
        # self.count = board["figures_count"]
        self.cells = dict()
        self.steps = []
        self.our_steps = []
        self.height = board["height"]
        self.first = 'Unknown'
        # self.not_used = dict()
        cells = board["cells"]
        for i in range(board["figures_count"]):
            self.cells[i] = Cell(i,self)
            
        for i, row in enumerate(cells):
            for j, cur_id in enumerate(row):
                cur_cell = self.cells[cells[i][j]]
                cur_cell.inc()
                if i != 0:
                    neigh_id = cells[i-1][j]
                    add_neigh(self.cells[neigh_id], cur_cell)
                if j != 0:
                    neigh_id = cells[i][j-1]
                    add_neigh(self.cells[neigh_id], cur_cell)
                if i % 2 == 0 and i > 0 and j > 0:
                    neigh_id = cells[i-1][j-1]
                    add_neigh(self.cells[neigh_id], cur_cell )
                elif i % 2 != 0 and i > 0 and j < len(row) - 1:
                    neigh_id = cells[i-1][j+1]
                    add_neigh(self.cells[neigh_id], cur_cell )
    def small(self):
        return self.height<11 

def add_neigh(cell, cur_cell):
    if cell.id != cur_cell.id:
        cur_cell.add(cell.id)
        cell.add(cur_cell.id)


class Cell:
    def __init__(self, id, game):
        self.game = game
        self.id = id
        # self.neigh = dict()
        self.neigh = set()
        self.color = -1
        self.count = 0

    def inc(self):
        self.count += 1

    def add(self, id):
        self.neigh.add(id)
        # self.neigh[id] = True

    def can_color(self, col):
        if self.color != -1:
            return False
        for neigh_id in self.neigh:
            c = self.game.cells[neigh_id]
            if c.color == col:
                return False
        return True

def max_count(game, col):    
    maximum = None
    game.first = (col == 0 or col == 2)

    for _, c in game.cells.items():
        if c.can_color(col):
            if maximum is None:
                maximum = c
            else:
                if maximum.count < c.count:
                    maximum = c
    #game.cells[maximum.id].color = col
    game.our_steps.append((maximum.id,col))
    return maximum.id


def register_step(game, fig, col):
    game.cells[fig].color = col
    game.steps.append((fig,col))
