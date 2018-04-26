""" docstring for user controller"""
import datetime
import re
import jwt
from email_validator import validate_email, EmailNotValidError
from passlib.hash import sha256_crypt
from flask import jsonify
from flask_mail import Message
from app import app, mail
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

    #forgot password
    def forgot_password(self, data):
        """
        check email, create reset password link
        """
        fields = ['email']
        result = self.check_req_fields(data, fields)
        if result["success"]:
        # validate user input
            user = User.email_exists(data)
            if not user:
                return jsonify({"success":False, "message":"User not found"}), 404
            # create verification link
            token = jwt.encode(
                {
                    'uid':user.id,
                    'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
                }, app.config['SECRET_KEY']).decode('UTF-8')
            user.save_reset_token(token)
            # create email instance
            msg = Message("Password Reset Link",
              sender="noreply@tbc.com",
              recipients=[user.email])
            msg.html = "<p>Hello <strong>" + user.name + "</strong>, use the "
            msg.html += "link provided to reset your password:"
            msg.html += "</p><a class='text-center' href="+ app.config['FRONT_END_URL']
            msg.html += "reset_password/"+ token + ">Reset Password</a>"
            msg.html += "<p>If it does not work, copy and paste this in the url: "
            msg.html +=  app.config["FRONT_END_URL"] + "reset_password/" + token +"</p>"

            mail.send(msg)

            return jsonify({"success":True,
                            "message":"A passsword reset link has been to: "+ user.email}), 200
        return jsonify(result), 422

    #verify password reset token
    def verify_password_token(self, data):
        """
        check email, create reset password link
        """
        fields = ['token']
        result = self.check_req_fields(data, fields)
        if result["success"]:
            # verifiry token
            try:
                decoded = jwt.decode(data["token"], app.config['SECRET_KEY'])
                current_user = decoded["uid"]
            except:
                return jsonify({"success":False, "token":False,
                                "message":"Password reset link is invalid or expired"}), 422
            user = User.get_token_user(current_user, data["token"])
            if not user:
                return jsonify({"success":False,
                                "message":"Password reset link has been used. Resend link"}), 404
            token = None
            user.save_reset_token(token)
            return jsonify({"success":True, "user":user.email}), 200
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
            if not bool(re.match('[A-Za-z]{2,50}( [A-Za-z]{2,25})?', data["name"])):
                return {"success":False, "message":"Invalid name"}

        # validate email
        if 'email' in data:
            if not bool(re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data["email"])):
                return {"success":False,
                        "message": "Email address must be in the format: abc@gmail.com"}

        # validate password
        if 'password' in data:
            if not re.match('^(?=.*?[a-z])(?=.*?[\d])(?=.*?[\W]).{6,80}$', data["password"]):
                return {"success":False,
                        "message":"Password should have 6 - 35 characters," +
                        "Include alphanumeric characters and upper case letters"}

        return {"success":True}
