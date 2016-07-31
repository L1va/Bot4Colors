games = dict()


class Game:
    def __init__(self, board):
        # self.count = board["figures_count"]
        self.cells = dict()
        # self.not_used = dict()
        cells = board["cells"]
        for i, row in enumerate(cells):
            for j, cur_id in enumerate(row):
                if cur_id in self.cells:
                    cur_cell = self.cells[cur_id]
                else:
                    cur_cell = Cell(cur_id, self)
                    self.cells[cur_id] = cur_cell
                    # self.not_used[cur_id] = True
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
        self.neigh = dict()
        self.color = -1

    def add(self, id):
        self.neigh[id] = True

    def can_color(self, color):
        for id, v in self.neigh.items():
            c = self.game.cells[id]
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
