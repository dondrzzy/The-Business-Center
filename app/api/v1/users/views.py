from flask import redirect, render_template, request, \
    url_for, Blueprint, jsonify
from app import app
from app.services.token_service import TokenService
from app import jwt

from app.services.user_service import UserService
US = UserService()
TS = TokenService()

""" config """

users_blueprint = Blueprint(
    'users', __name__
)

# routes
@users_blueprint.route('/api/v1/auth/register', methods=['POST'])
def register():
    """" register a user route """
    data = request.get_json()
    result = US.register_user(data)

    return result

@users_blueprint.route('/api/v1/auth/login', methods=['POST'])
def login():
    """login route """
    data = request.get_json()

    # check if token in headers
    # if 'x-access-token' in request.headers:
    #     token = request.headers['x-access-token']
    #     # check if logged already
    #     if US.user_logged_in(token, data):
    #         return jsonify({"success":False, "msg":"Already logged in... Redirecting"})

    result = US.login_user(data)

    return result



@users_blueprint.route('/api/v1/auth/logout', methods=['GET'])
def logout():
    """ logout route """
    token = None

    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']

    if not token:
        return jsonify({'success':False, 'token':False, 'message':'Token is missing'}),401

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'success':False, 'token':data, 'message':'Token is invalid'}),401

    return jsonify(TS.blacklist(token)),200

@users_blueprint.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ reset a password """
    data = request.get_json()
    return US.reset_password(data)