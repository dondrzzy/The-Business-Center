""" docstring for user controller"""
import datetime
import re
import jwt
from email_validator import validate_email, EmailNotValidError
from passlib.hash import sha256_crypt
from flask import jsonify
from app import app
from app.models.user import User
from app.services.token_service import TokenService

# instatiate models
TS = TokenService()

class UserService(object):
    """docstring for UserController"""
    def __init__(self, argz=0):
        self.argz = argz

    def register_user(self, data):
        """docstring for registering a  user account """
        fields = ['name', 'email', 'password', 'confirm_password']
        result = self.check_req_fields(data, fields, True)

        if result["success"]:
            # validate user emails
            valid_input_res = self.validate_user_input(data)
            if valid_input_res["success"]:
                # check if email exists
                user = User.email_exists(data)
                if not user:
                    # create user
                    User(name=data["name"], email=data["email"],
                         password=sha256_crypt.encrypt(str(data["password"]))).register()
                    return jsonify({"success":True, "message":"Account created successfully"}), 201
                return jsonify({"success":False, "message":"Email already exists"}), 409
            return jsonify(valid_input_res), 422
        return jsonify(result), 422

    # login user
    def login_user(self, data):
        """ login in user """
        fields = ['email', 'password']
        result = self.check_req_fields(data, fields)
        if result["success"]:

            # check if email exists in the db
            user = User.email_exists(data)
            if not user:
                return jsonify({"success":False, "message":"User not found"}), 404

            # If user found, confirm passwords and create token
            # check if passwords match
            if sha256_crypt.verify(data["password"], user.password):
                token = jwt.encode(
                    {
                        'uid':user.id,
                        'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
                    }, app.config['SECRET_KEY'])

                return jsonify({"success":True, "token":token.decode('UTF-8')}), 200

            return jsonify({"success":False, "message":"Incorrect username or password"}), 401

        return jsonify(result), 422

    # reset password
    def reset_password(self, data):
        """
            reset a password
            using data coming in from the view
            returns res from
        """
        fields = ['email', 'password', 'confirm_password']
        result = self.check_req_fields(data, fields, True)
        if result["success"]:
            # validate user input
            valid_input_res = self.validate_user_input(data)
            if valid_input_res["success"]:
                user = User.email_exists(data)
                if not user:
                    return jsonify({"success":False, "message":"User not found"}), 404
                user_object = {
                    "email" : data["email"],
                    "password" : sha256_crypt.encrypt(str(data["password"]))
                }

                User.reset_password(user_object)
                return jsonify({"success":True, "message":"Password reset successfully"}), 200
            return jsonify(valid_input_res), 422
        return jsonify(result), 422

    @staticmethod
    def user_logged_in(token, data):
        """ check token """

        try:
            token_data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = token_data["uid"]
            # check if logged out
            if TS.is_blacklisted(token)["success"]:
                return False
            # get user if exists
            user = User.get_user(current_user)
            if user.email == data["email"]:
                return True
        except:
            return False

    @staticmethod
    def check_req_fields(_object, fields, comp_pwds=False):
        """checks required fields"""
        for field in fields:
            if field not in _object:
                return {"success":False, "message":field + " is required"}
        if comp_pwds:
            if _object["password"] != _object["confirm_password"]:
                return {"success":False, "message":"passwords do not match"}
        return {"success":True}

    @staticmethod
    def validate_user_input(data):
        """ validate user''s name, email, password strength """
        # validate name
        if 'name' in data:
            if not bool(re.fullmatch('[A-Za-z]{2,50}( [A-Za-z]{2,25})?', data["name"])):
                return {"success":False, "message":"Invalid name"}

        # validate email
        if 'email' in data:
            if len(data["email"]) > 50:
                return {"success":False,
                        "message":"Email address should not exceed 50 characters"}
            try:
                validate_email(data["email"]) # validate and get info
            except EmailNotValidError as error:
                # email is not valid, exception message is human-readable
                return {"success":False, "message":str(error)}

        # validate password
        if 'password' in data:
            if not re.match('^(?=.*?[a-z])(?=.*?[\d])(?=.*?[\W]).{6,80}$', data["password"]):
                return {"success":False, "message":"Password should have 6 - 35 characters,\
                        Include alphanumeric characters and upper case letters"}

        return {"success":True}
