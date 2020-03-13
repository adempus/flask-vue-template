from core import db, signUpUser, signInUser, getAppKey, getDBCredentials, requireAuthentication, decodeSessionToken
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
    appInstance.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials('db_credentials.json')
    appInstance.config['SECRET_KEY'] = getAppKey('app_key.json')
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


@app.route('/protected-route', methods=['GET'])
@requireAuthentication(app)
def protectedTestRoute():
    data = decodeSessionToken(app)
    return jsonify(data)


@app.route('/user/<userId>', methods=['GET'])
@requireAuthentication(app)
def userPage(userId):
    print(f'user id: {userId}')
    data = decodeSessionToken(app)
    return jsonify(data)


@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        signUpData = dict(request.get_json())
        resPayload = signUpUser(signUpData)
        return jsonify(resPayload)


@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        signInData = dict(request.get_json())
        resPayload = signInUser(signInData, app.config['SECRET_KEY'])
        return resPayload


app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run(debug=True)
