

games = dict()

class Game:
    def __init__(self, board):
        print(board)
        self.count = board["figures_count"]
        self.used = []


def max_count(id, color):
    game = games[id]
    for i in range(game.count):
        if i not in game.used:
            game.used.append(i)
            return i
    return 0

def enemy_step(id, fig, color):
    game = games[id]
    game.used.append(fig)