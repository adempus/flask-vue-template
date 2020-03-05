import os
import json
import bcrypt
import jwt
import datetime
from functools import wraps
from flask import request
from core import db, User


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
        firstName, lastName, username = user['firstName'], user['lastName'], user['userName']
        email, password = user['email'], user['password']
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
        if True in signInErrors.values():
            return { 'error': True, 'message': signInErrors }
        else:
            savedPassword = userQuery.password
            match = bcrypt.checkpw(password.encode(), savedPassword.encode())
            if not match:
                signInErrors['passwordInvalid'] = not match
                return { 'error': True, 'message': signInErrors }
            else:
                sessionToken = generateSessionToken({'user': getSignInPayload(userQuery)}, appKey)
                return {
                    'error': False,
                    'message': signInErrors,
                    'user': { 'id': userQuery.id, 'data': sessionToken.decode('UTF-8') }
                }


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
    sessionToken = request.args.get('token')
    if sessionToken:
        try:
            data = jwt.decode(sessionToken, app.secret_key, algorithms=['HS256'])
            data['error'] = False
            return data
        except jwt.InvalidTokenError as err:
            return { 'error': True, 'message': 'Invalid session token provided.' }


def requireAuthentication(app):
    def authDecorator(funct):
        @wraps(funct)
        def authWrapper(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return { 'error': True, 'message': 'No session token provided.' }
            try:
                jwt.decode(token, app.secret_key, algorithms=['HS256'])
            except jwt.InvalidTokenError as err:
                print(f"error: {err}")
                return { 'error': True, 'message': 'Invalid session token provided.' }
            return funct(*args, **kwargs)
        return authWrapper
    return authDecorator


