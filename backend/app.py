from flask import Flask, jsonify
from flask_cors import CORS


DEBUG = True

# app instance
app = Flask(__name__)
app.config.from_object(__name__)

# CORS setup
CORS(app, resources={ r'/*': {'origins': '*' }})


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test-route', methods=['GET'])
def testRoute():
    return jsonify({'td1': 'first', 'td2': 'second', 'td3': 'third', 'td4': 'fourth'})


if __name__ == '__main__':
    app.run()
