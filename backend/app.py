from core import db, signUpUser, signInUser, getAppKey, getDBCredentials, requireAuthentication, decodeSessionToken, \
    postNewUserEntry, getUserEntries, getUserId, deleteUserEntry

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
    appInstance.config['SQLALCHEMY_DATABASE_URI'] = getDBCredentials(
        '/home/adempus/Projects/flask-vue-template/backend/db_credentials.json'
    )
    appInstance.config['SECRET_KEY'] = getAppKey('/home/adempus/Projects/flask-vue-template/backend/app_key.json')
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


@app.route('/authenticate', methods=['GET'])
@requireAuthentication(app)
def authenticationRoute():
    data = decodeSessionToken(app)
    return jsonify(data)


@app.route('/user/<userId>', methods=['GET'])
@requireAuthentication(app)
def userPage(userId):
    print(f'user id: {userId}')
    data = decodeSessionToken(app)
    if data['data']['user']['id'] != int(userId):
        return {
            'error': True,
            'message': '401 Unauthorized. \nUser does not have permission to access this route.'
        }
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


@app.route('/post-new-entry', methods=['POST'])
@requireAuthentication(app)
def postNewUserLog():
    if request.method == 'POST':
        entryData = dict(request.get_json())
        resPayload = postNewUserEntry(entryData)
        return jsonify(resPayload)


@app.route('/get-user-entries', methods=['GET'])
@requireAuthentication(app)
def getUserLogs():
    userId = getUserId(app)
    userEntries = getUserEntries(userId)
    print(f"userEntries: {userEntries}")
    return { 'error': False, 'data': userEntries }


@app.route('/delete-user-entry', methods=['DELETE'])
@requireAuthentication(app)
def deleteUserLog():
    deletionPayload = dict(request.get_json())
    deletionResponse = deleteUserEntry(deletionPayload)
    return jsonify(deletionResponse)


if __name__ == '__main__':
    # app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', threaded=True, debug=True, port=5000)

