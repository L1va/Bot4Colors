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
                    add_neigh(cells[i-1][j], cur_id, cur_cell, self.cells)
                if j != 0:
                    add_neigh(cells[i][j-1], cur_id, cur_cell, self.cells)
                if i % 2 == 0 and i > 0 and j > 0:
                    add_neigh(cells[i-1][j-1], cur_id, cur_cell, self.cells)
                elif i % 2 != 0 and i > 0 and j < len(row) - 1:
                    add_neigh(cells[i-1][j+1], cur_id, cur_cell, self.cells)


def add_neigh(id, cur_id, cur_cell, cells):
    if id != cur_id:
        cur_cell.add(id)
        left_c = cells[id]
        left_c.add(cur_id)


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
        # for id, v in self.neigh.items():
        for neigh_id in self.neigh:
            c = self.game.cells[neigh_id]
            if c.color == color:
                return False
        return True


def max_count(id, color):
    game = games[id]
    for id, c in game.cells.items():
        if c.color == -1 and c.can_color(color):
            c.color = color
            return id


def enemy_step(id, fig, color):
    game = games[id]
    game.cells[fig].color = color
