from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(500), nullable=False)
    middlename = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    confirmed = db.Column(db.Boolean, unique=False, default=False)
    city = db.Column(db.String(100), nullable=True)
    county = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return 'User>>> {self.email}'


class ZipCodesRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(5), nullable=False)
    county = db.Column(db.String(100), nullable=True)
    ocurrences = db.Column(db.Float, nullable=True)

    def __repr__(self) -> str:
        return 'ZipCodesRatings>>> {self.id}'