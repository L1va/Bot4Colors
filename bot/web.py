from flask import Flask, request, jsonify

from bot.first import *
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
    logger.info('New game handler')
    logger.info('Board data: %s', board)

    games[id] = Game(board)
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['GET'])
def get_game_handler(id):
    logger = make_logger(app.logger, id)
    logger.info('[GET] game. Our turn.')
    logger.info('Color is %s', request.args['color'])
    logger.info('Calculate turn')

    answer = max_count(id, request.args["color"])

    return jsonify(status='ok', figure=answer)


@app.route('/games/<string:id>', methods=['PUT'])
def put_handler(id):
    logger = make_logger(app.logger, id)

    data = request.json

    logger.info(
        '[PUT] Enemy turn is: figure %s with color %s',
        data['figure'], data['color'])
    logger.info('Register enemy step.')

    enemy_step(id, data["figure"], data["color"])
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['DELETE'])
def delete_handler(id):
    logger = make_logger(app.logger, id)

    logger.info('[DELETE] End of game')

    try:
        del games[id]
    except:
        logger.exception('Error while deliting game from memory.')

    return jsonify(status='ok')
