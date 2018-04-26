""" routes for the user model """
from flask import request, Blueprint, jsonify
from app import app
from app.services.token_service import TokenService
from app import jwt

from app.services.user_service import UserService
US = UserService()
TS = TokenService()

""" config """

USERS_BLUEPRINT = Blueprint(
    'users', __name__
)

# routes
@USERS_BLUEPRINT.route('/register', methods=['POST'])
def register():
    """" register a user route """
    data = request.get_json()
    result = US.register_user(data)

    return result

@USERS_BLUEPRINT.route('/login', methods=['POST'])
def login():
    """login route """
    data = request.get_json()

    # check if token in headers
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
        # check if logged already
        if US.user_logged_in(token, data):
            return jsonify({"success":False, "message":"Already logged in... Redirecting"}), 200

    return US.login_user(data)



@USERS_BLUEPRINT.route('/logout', methods=['GET'])
def logout():
    """ logout route """
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
    if not token:
        return jsonify({'success':False, 'message':'Token is missing', 'token':False}), 401
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'success':False, 'message':'Token is invalid', 'token':False}), 401

    return jsonify(TS.blacklist(token)), 200

@USERS_BLUEPRINT.route('/reset-password', methods=['POST'])
def reset_password():
    """ reset a password """
    data = request.get_json()
    return US.reset_password(data)

@USERS_BLUEPRINT.route('/forgot-password', methods=['POST'])
def forgot_password():
    """ reset a password """
    data = request.get_json()
    return US.forgot_password(data)

@USERS_BLUEPRINT.route('/verify-password-token', methods=['POST'])
def verify_password_token():
    """ verify reset token """
    data = request.get_json()
    return US.verify_password_token(data)
