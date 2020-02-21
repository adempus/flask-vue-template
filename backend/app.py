from core import db, signUpUser, signInUser
from core import getDBCredentials
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

DEBUG = True

def create_app():
    appInstance = Flask(__name__)
    appInstance.config.from_object(__name__)
    # CORS setup
    CORS(appInstance, resources={r'/*': {'origins': '*'}})
    appInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    appInstance.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials()
    return appInstance


app = create_app()
app.app_context().push()
# database initialization
db.init_app(app)
migrate = Migrate(app, db)

""" ***********  backend routes  ************* """


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test-route', methods=['GET'])
def testRoute():
    return jsonify({'td1': 'first', 'td2': 'second', 'td3': 'third', 'td4': 'fourth', 'td5': 'fifth'})


@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        signUpData = dict(request.get_json())
        # print(f"sign-up data: \n{signUpData}")
        resPayload = signUpUser(signUpData)
        return jsonify(resPayload)


@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        signInData = dict(request.get_json())
        # print(f"sign-in data: \n{signInData}")
        resPayload = signInUser(signInData)
        return jsonify(resPayload)


if __name__ == '__main__':
    app.run()

