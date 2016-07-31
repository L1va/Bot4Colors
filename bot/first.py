
from collections import Counter
import operator
games = dict()

class Game:
    def __init__(self, board):
        print(board)
        self.count = board["figures_count"]
        c = Counter()
        for row in board["cells"]:
            c.update(row)
        self.cnt = dict(c)
        self.used = []


def max_count(id, color):
    game = games[id]
    fig, count = min(game.cnt.items(), key=operator.itemgetter(1))
    use(game, fig)
    return fig
    # for i in range(game.count):
    #     if i not in game.used:
    #         game.used.append(i)
    #         return i
    # return 0

def use(game, fig):
    del game.cnt[fig]

def enemy_step(id, fig, color):
    game = games[id]
    use(game, fig)
    #game.used.append(fig)