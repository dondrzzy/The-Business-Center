from flask import redirect, render_template, request, \
    url_for, Blueprint, jsonify
from app import is_logged_in

from app.services.user_service import UserService
US = UserService()

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

    return jsonify(result) 

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

    return jsonify(result)



@users_blueprint.route('/api/v1/auth/logout', methods=['POST'])
@is_logged_in
def logout():
    """ logout route """
    return jsonify({"success":True, "msg":"You are logged out"})

@users_blueprint.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ reset a password """
    data = request.get_json()
    return jsonify(US.reset_password(data))