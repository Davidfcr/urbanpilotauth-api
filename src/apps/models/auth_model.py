from src.db import User, db


def user_exists_by_email(email):
    return User.query.filter_by(email=email).first() is not None

def save_user(email, firstname, middlename, lastname, zipcode):
    model = User(email=email, firstname=firstname, middlename=middlename, lastname=lastname, zipcode=zipcode)
    db.session.add(model)
    db.session.commit()
    return model