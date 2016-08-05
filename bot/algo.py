games = dict()


class Game:
    def small(self):
        return self.height<11 

    def __init__(self, board):
        self.cells = dict()
        self.steps = []
        self.our_steps = []
        self.height = board["height"]
        self.first = 'Unknown'
        self.start_from = 0
        cells = board["cells"]
        for i in range(board["figures_count"]):
            self.cells[i] = Cell(i,self)
            
        for i, row in enumerate(cells):
            for j, cur_id in enumerate(row):
                cur_cell = self.cells[cells[i][j]]
                cur_cell.inc()
                if i != 0:
                    neigh_id = cells[i-1][j]
                    cur_cell.add_neigh(self.cells[neigh_id])
                if j != 0:
                    neigh_id = cells[i][j-1]
                    cur_cell.add_neigh(self.cells[neigh_id])
                if i % 2 == 0 and i > 0 and j > 0:
                    neigh_id = cells[i-1][j-1]
                    cur_cell.add_neigh(self.cells[neigh_id])
                elif i % 2 != 0 and i > 0 and j < len(row) - 1:
                    neigh_id = cells[i-1][j+1]
                    cur_cell.add_neigh(self.cells[neigh_id])

class Cell:
    def __init__(self, id, game):
        self.game = game
        self.id = id
        self.neigh = set()
        self.color = -1
        self.count = 0

    def inc(self):
        self.count += 1

    def add_neigh(self, cell):
        if self.id != cell.id:
            self.neigh.add(cell.id)
            cell.neigh.add(self.id)

    def is_neigh(self, cell):
        return cell.id in self.neigh

    def can_color(self, col):
        for neigh_id in self.neigh:
            c = self.game.cells[neigh_id]
            if c.color == col:
                return False
        return True

def byCount(cell): #colored - in the end
    if cell.color!=-1:
        return 1
    return -cell.count

def best_step(game, col):    
    game.first = (col == 0 or col == 2)
    nextCol = (col + 1) % 4

    cells = sorted(game.cells.values(), key = byCount)

    best = None
    cells_to_choose = []
    for c in cells:
        if c.color!=-1:
            break
        if best is not None and best.count - c.count > 3:
            break
        if c.can_color(col):
            if best is None:
                best = c
            if c.can_color(nextCol):
                cells_to_choose.append(c)                
    
    if len(cells_to_choose)>0:
        best = try_to_select(cells_to_choose)

    game.our_steps.append((best.id,col))
    return best.id

def try_to_select(cells):
    best = cells[0]
    bestv = 0
    size = len(cells)
    for i in range(size):
        cur = cells[i].count
        for j in range(size):
            if i == j:
                continue
            if not cells[i].is_neigh(cells[j]):
                cur+= cells[j].count
        if cur > bestv:
            bestv = cur
            best = cells[i]
    return best


def register_step(game, fig, col):
    game.cells[fig].color = col
    game.steps.append((fig,col))
