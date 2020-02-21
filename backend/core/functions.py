import json
import bcrypt
from core import db, User


def getDBCredentials():
    with open('../backend/db_credentials.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"


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


def signInUser(user):
    if None not in user.values():
        email, password = user['email'], user['password']
        userQuery = User.query.filter_by(email=email).first()
        signInError = {
            'userNotFound': userQuery is None,
            'passwordInvalid': False
        }
        if True in signInError.values():
            return { 'error': True, 'message': signInError }
        else:
            savedPassword = userQuery.password
            match = bcrypt.checkpw(password.encode(), savedPassword.encode())
            if not match:
                signInError['passwordInvalid'] = not match
                return { 'error': True, 'message': signInError }
            else:
                print(f"user signed in with id: {userQuery.id}")
                return { 'error': False, 'message': signInError, 'user': { 'id': userQuery.id } }


def getHashedPass(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)