from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(75), unique=False, nullable=False)
    last_name = db.Column(db.String(75), unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    entries = db.relationship('Entry', backref='user', lazy=True)

    def __init__(self, firstName, lastName, userName, email, password):
        self.first_name = firstName
        self.last_name = lastName
        self.username = userName
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Entry(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(30), nullable=True)
    content = db.Column(db.Text, nullable=False)
    entryDate = db.Column(db.DateTime, nullable=False)
    userId = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, userId, title, content, entryDate):
        self.userId = userId
        self.title = title
        self.content = content
        self.entryDate = entryDate

    def __repr__(self):
        return '<Entry %r>' % self.id
