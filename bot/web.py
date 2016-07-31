from flask import Flask, request, jsonify

from bot.first import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/games', methods=['POST'])
def new_game_handler():
    print(request.json)
    id = request.json["id"]
    board = request.json["board"]
    games[id] = Game(board)  
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['GET'])
def get_game_handler(id):
    print('[GET] games/:id')
    print(id)
    print(request.args)
    return jsonify(status='ok', figure=max_count(id, request.args["color"]))


@app.route('/games/<string:id>', methods=['PUT'])
def put_handler(id):
    print('[PUT] games/:id')
    print(id)
    data = request.json
    print(data)
    enemy_step(id, data["figure"], data["color"])
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['DELETE'])
def delete_handler(id):
    print('[DELETE] /games/:id')
    print(id)
    del games[id]
    return jsonify(status='ok')
