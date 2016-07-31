games = dict()


class Game:
    def __init__(self, board):
        # self.count = board["figures_count"]
        self.cells = dict()
        # self.not_used = dict()
        cells = board["cells"]
        for i in range(board["figures_count"]):
            self.cells[i] = Cell(i,self)
            self.cells[i].inc()

        for i, row in enumerate(cells):
            for j, cur_id in enumerate(row):
                cur_cell = self.cells[cells[i][j]]
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

def max_count(id, col):
    game = games[id]
    maximum = None

    for id, c in game.cells.items():
        if c.can_color(col):
            if maximum is None:
                maximum = c
            else:
                if maximum.count < c.count:
                    maximum = c
    return maximum.id


def enemy_step(id, fig, col):
    game = games[id]
    game.cells[fig].color = col
