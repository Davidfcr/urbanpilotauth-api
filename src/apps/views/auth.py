from src.constants.http_status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from flask import Blueprint, jsonify, request
from src.db import User, db
from src.apps.models.auth_model import user_exists_by_email, save_user
from src.services import zipcode_services
import validators

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():
    email = request.json['email']
    firstname = request.json['firstname']
    middlename = request.json['middlename']
    lastname = request.json['lastname']
    zipcode = request.json['zipcode']
    
    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    if user_exists_by_email(email):
        return jsonify({'error': "Email already exits"}), HTTP_409_CONFLICT

    if firstname is None:
        return jsonify({'error': "First Name can not be empty"}), HTTP_400_BAD_REQUEST

    if lastname is None:
        return jsonify({'error': "Last Name can not be empty"}), HTTP_400_BAD_REQUEST

    if not zipcode.isnumeric():
        return jsonify({'error': "Zip Code should be numeric"}), HTTP_400_BAD_REQUEST

    if zipcode is None:
        return jsonify({'error': "Zip Code can not be empty"}), HTTP_400_BAD_REQUEST
        
    if len(zipcode) != 5:
        return jsonify({'error': "Zip Code is not valid, a 5 digits zip code is required"}), HTTP_400_BAD_REQUEST

    
    user = save_user(email, firstname, middlename, lastname, zipcode)
    zipcode_services.identify_zipcode(user)

    return jsonify({
        'message': "User created",
        'user': {
            "id": user.id, 
            "email": user.email,
            "firstname": user.firstname, 
            "middlename": user.middlename,
            "lastname": user.lastname,
            "zipcode": user.zipcode
        }

    }), HTTP_201_CREATED
