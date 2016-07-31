import json


from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/games', methods=['POST'])
def new_game_handler():
    print(request.json)
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['GET'])
def get_game_handler(id):
    print('[GET] games/:id')
    print(id)
    print(request.args)
    return jsonify(status='ok', figure=0)


@app.route('/games/<string:id>', methods=['PUT'])
def put_handler(id):
    print('[PUT] games/:id')
    print(id)
    data = json.loads(request.data)
    print(data)
    return jsonify(status='ok')


@app.route('/games/<string:id>', methods=['DELETE'])
def delete_handler(id):
    print('[DELETE] /games/:id')
    print(id)
    return jsonify(status='ok')
