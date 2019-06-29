from flask import (
    Blueprint, g, request, jsonify
)
from .db import *
from .authUtil import authenticate
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    query = "INSERT INTO users (username, pass) VALUES('%s', '%s')"%(username, password)
    try:
        update_query(query)
    except Exception as e:
        return (str(e))
    return jsonify({"status": "success"})

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = authenticate(username, password)
    if user is None:
        return jsonify({"Error": "Bad Username or Password"}), 401
    access_token = create_access_token(identity = username)
    return jsonify({"status": "success", "access_token": access_token})

@bp.route('/protected')
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify({"logged_in_as": current_user})
