import pytest
from sqlalchemy import delete
from src import create_app
from src.db import db, User

@pytest.fixture(scope="session")
def flask_app():
    app = create_app()
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()
    yield client
    ctx.pop()

@pytest.fixture(scope="session")
def app_with_db(flask_app):
    db.create_all()
    yield flask_app
    db.session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):
    user = User()
    user.email = "davidfcr@live.com"
    user.firstname = "David"
    user.lastname = "Cardenas"
    user.zipcode = "43460"
    db.session.add(user)
    db.session.commit()
    yield app_with_db
    db.session.execute(delete(User))
    db.session.commit()