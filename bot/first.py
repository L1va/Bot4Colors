games = dict()


class Game:
    def __init__(self, board):
        # self.count = board["figures_count"]
        self.cells = dict()
        # self.not_used = dict()
        cells = board["cells"]
        for i, row in enumerate(cells):
            for j, cur_id in enumerate(row):
                cur_cell = self.cells.setdefault(cur_id, Cell(cur_id, self))
                if i != 0:
                    add_neigh(self.cells[cells[i-1][j]], cur_cell)
                if j != 0:
                    add_neigh(self.cells[cells[i][j-1]], cur_cell)
                if i % 2 == 0 and i > 0 and j > 0:
                    add_neigh(self.cells[cells[i-1][j-1]], cur_cell )
                elif i % 2 != 0 and i > 0 and j < len(row) - 1:
                    add_neigh(self.cells[cells[i-1][j+1]], cur_cell )
        print("####### neigh:")
        print(board)
        for id,c in self.cells.items():
            print(c.id, c.neigh)


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

    def add(self, id):
        self.neigh.add(id)
        # self.neigh[id] = True

    def can_color(self, color):
        if self.color != -1:
            return False
        for neigh_id in self.neigh:
            c = self.game.cells[neigh_id]
            if c.color == color:
                return False
        return True


def max_count(id, color):
    game = games[id]
    for id, c in game.cells.items():
        if c.can_color(color):
            game.cells[id].color = color
            return id


def enemy_step(id, fig, color):
    game = games[id]
    game.cells[fig].color = color
