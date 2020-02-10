from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(75), unique=False, nullable=False)
    last_name = db.Column(db.String(75), unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username