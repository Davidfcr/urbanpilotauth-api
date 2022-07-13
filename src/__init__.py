from flask import Flask
from flask.json import jsonify
import os
from src.db import db
from src.apps.views.auth import auth
from src.constants.http_status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(config)


    db.app = app
    db.init_app(app)

    app.register_blueprint(auth)
    

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return jsonify({'error': 'Internal server error'}), HTTP_500_INTERNAL_SERVER_ERROR

    return app