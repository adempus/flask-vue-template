import json

def getDBCredentials():
    with open('/home/adempus/Projects/flask-vue-template/backend/db_credentials.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    return f"{data['driver']}://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['db']}"