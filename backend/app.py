from core import db
from core import getDBCredentials
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

DEBUG =True

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    # CORS setup
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials()
    return app

app = create_app()
app.app_context().push()
# database initialization
db.init_app(app)
migrate = Migrate(app, db)


'''***********  backend routes  *************'''


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test-route', methods=['GET'])
def testRoute():
    return jsonify({'td1': 'first', 'td2': 'second', 'td3': 'third', 'td4': 'fourth', 'td5': 'fifth'})


if __name__ == '__main__':
    app.run()
