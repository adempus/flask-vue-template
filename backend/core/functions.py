import json
import bcrypt
import jwt
import datetime
from functools import wraps
from flask import request, make_response
from core import db, User, Entry
from sqlalchemy import desc


def getDBCredentials(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"


def getAppKey(path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
    return data['app_key']


def signUpUser(user):
    if None not in user.values():
        email, username = user['email'], user['userName']
        emailQuery = User.query.filter_by(email=email).first()
        usernameQuery = User.query.filter_by(username=username).first()
        dbRecordConflict = {
            'emailExists': emailQuery is not None,
            'usernameExists': usernameQuery is not None
        }
        if True in dbRecordConflict.values():
            print(f"There is a record containing username, and/or email: {dbRecordConflict}")
            return { 'error': True, 'message': dbRecordConflict }
        else:
            firstName, lastName, password = user['firstName'], user['lastName'], user['password']
            newUser = User(firstName, lastName, username, email, getHashedPass(password))
            db.session.add(newUser)
            db.session.commit()
            print(f"newly created user: {newUser}")
            return {'error': False, 'message': f'new user id: {newUser.id}'}
    else:
        return {'error': True, 'message': 'invalid payload'}


def signInUser(user, appKey):
    if None not in user.values():
        email, password = user['email'], user['password']
        userQuery = User.query.filter_by(email=email).first()
        signInErrors = {
            'userNotFound': userQuery is None,
            'passwordInvalid': False
        }
        if signInErrors['userNotFound']:
            return { 'error': True, 'message': signInErrors }
        else:
            savedPassword = userQuery.password
            signInErrors['passwordInvalid'] = not bcrypt.checkpw(password.encode(), savedPassword.encode())
            if signInErrors['passwordInvalid']:
                return { 'error': True, 'message': signInErrors }
            else:
                sessionToken = generateSessionToken({'user': getSignInPayload(userQuery)}, appKey)
                response = make_response({
                    'error': False,
                    'token': sessionToken.decode('UTF-8'),
                    'data': getSignInPayload(userQuery)
                })
                response.headers['Authorization'] = f'Bearer {sessionToken}'
                return response


def postNewUserEntry(entryData):
    if not None in entryData.values():
        title, content, userId = entryData['title'], entryData['entry'], entryData['userId']
        timestamp = datetime.datetime.now()
        if len(title) < 1: title = None
        newEntry = Entry(userId, title, content, timestamp)
        db.session.add(newEntry)
        db.session.commit()
        print(f"new entry submitted: {entryData}")
        return {'error': False, 'message': 'Entry post successful'}
    else:
        return {'error': True, 'message': 'Entry post error. (no content)'}


def getUserEntries(userId):
    if userId is not None:
        entryQuery = Entry.query.filter_by(userId=userId).order_by(desc(Entry.entryDate)).all()
        userEntries = [
            {
                'id': e.id,
                'title': e.title,
                'content': e.content,
                'date': e.entryDate.strftime("%a, %B %d, %Y @ %I:%M %p")
            }
            for e in entryQuery
        ]
        return userEntries
    return {'error': True, 'message': 'user ID is null'}


def deleteUserEntry(deletionData):
    if len(deletionData) > 0:
        entryId = deletionData['id']
        entryQuery = Entry.query.filter_by(id=entryId).first()
        if entryQuery is not None:
            db.session.delete(entryQuery)
            print(f"deleted entry record {id}")
            db.session.commit()
            return {'error': False, 'message': f"entry {deletionData['title']} deleted successfully. "}
        return {'error': True, 'message': 'Could not find the entry record provided.'}
    return {'error': True, 'message': 'no deletion data provided. '}


def getSignInPayload(query):
    return {
        'id': query.id,
        'firstName': query.first_name,
        'username': query.username
    }


def getHashedPass(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def generateSessionToken(payload, appKey):
    return jwt.encode({
        'data': payload, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, appKey, algorithm='HS256')


def decodeSessionToken(app):
    sessionToken = getAuthToken()
    if sessionToken:
        try:
            data = jwt.decode(sessionToken, app.secret_key, algorithms=['HS256'])
            data['error'] = False
            return data
        except jwt.InvalidTokenError as err:
            print(f"Error: {err}")
            return { 'error': True, 'message': f'401 Unauthorized.\n Invalid session token provided. ({err}).' }


def requireAuthentication(app):
    def authDecorator(funct):
        @wraps(funct)
        def authWrapper(*args, **kwargs):
            token = getAuthToken()
            print(f'token from request headers: {token}')
            if not token:
                return { 'error': True, 'message': 'No session token provided.' }
            try:
                jwt.decode(token, app.secret_key, algorithms=['HS256'])
            except jwt.InvalidTokenError as err:
                print(f"error: {err}")
                return { 'error': True, 'message': f'401 Unauthorized.\n Invalid session token provided. ({err}).' }
            return funct(*args, **kwargs)
        return authWrapper
    return authDecorator


def getAuthToken():
    token = request.headers.get('Authorization')
    if token:
        return token.split(' ')[1]  # remove 'Bearer' part of token
    return None

def getUserId(app):
    userData = decodeSessionToken(app)
    return userData['data']['user']['id']

