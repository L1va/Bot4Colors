from flask import Flask, request, jsonify

from bot.algo import *
from bot.db import *
from bot.utils.log import make_logger

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/games', methods=['POST'])
def new_game_handler():
    id = request.json["id"]
    board = request.json["board"]

    logger = make_logger(app.logger, id)
    #logger.info('New game handler')
    newGame = Game(board)
    redis_set(id, newGame)
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['GET'])
def get_game_handler(id):
    logger = make_logger(app.logger, id)
    #logger.info('[GET] game. Our turn.')
    #logger.info('Color is %s', request.args['color'])
    #logger.info('Calculate turn')

    game = redis_get(id)
    answer = max_count(game, request.args["color"])
    redis_set(id, game)
    #logger.info('Our answer %s', answer)

    return jsonify(status='ok', figure=answer)


@app.route('/games/<string:id>', methods=['PUT'])
def put_handler(id):
    logger = make_logger(app.logger, id)

    data = request.json

    #logger.info('[PUT] Enemy turn is: figure %s with color %s', data['figure'], data['color'])
    #logger.info('Register enemy step.')

    game = redis_get(id)
    register_step(game, data["figure"], data["color"])
    redis_set(id, game)
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['DELETE'])
def delete_handler(id):
    logger = make_logger(app.logger, id)

    #logger.info('[DELETE] End of game')

    try:
        game = redis_get(id)
        if game.small():
            logger.info('game, first: %s', game.first)
            for _,c in game.cells.items():
                logger.info('%s[%s] -> %s', c.id, c.color, c.neigh )
            logger.info('our: %s', game.our_steps)
            logger.info('all: %s', game.steps)

        redis_del(id)
    except:
        logger.exception('Error while deliting game from memory.')

    return jsonify(status='ok')
