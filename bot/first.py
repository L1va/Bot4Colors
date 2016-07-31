
from collections import Counter
games = dict()

class Game:
    def __init__(self, board):
        print(board)
        self.count = board["figures_count"]
        self.cnt = Counter()
        for row in board["cells"]:
            self.cnt.update(row)
        self.used = []


def max_count(id, color):
    game = games[id]
    fig, count = game.cnt.most_common(1)[0]
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