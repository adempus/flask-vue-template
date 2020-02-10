from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

def getDBCredentials():
    db_uri = 'mysql://adempus:09sIUDpjhXjnfyJ@localhost/flask_vue_db'
    with open('./db_credentials.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"


# enable debugging
DEBUG = True
# app instance
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials()

db = SQLAlchemy(app)

# CORS setup
CORS(app, resources={ r'/*': {'origins': '*' }})


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test-route', methods=['GET'])
def testRoute():
    return jsonify({'td1': 'first', 'td2': 'second', 'td3': 'third', 'td4': 'fourth', 'td5': 'fifth'})


if __name__ == '__main__':
    app.run()
