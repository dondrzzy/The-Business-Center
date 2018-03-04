""" docstring for user controller"""
import datetime
import jwt
from passlib.hash import sha256_crypt
from app import jsonify
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

            # check if email exists
            if User.email_exists(data["email"])["success"]:
                return jsonify({"success":False, "message":"Email already exists"}), 400

            # create user
            User(name=data["name"], email=data["email"],
                 password=sha256_crypt.encrypt(str(data["password"]))).register()
            return jsonify({"success":True, "message":"Account created successfully"}), 201
        return jsonify(result), 400

    # login user
    def login_user(self, data):
        """ login in user """
        fields = ['email', 'password']
        result = self.check_req_fields(data, fields)
        if result["success"]:

            # check if email exists in the db
            user_result = User.is_member(data)

            # If user found, confirm passwords and create token
            if user_result["success"]:
                member = user_result["user"]
                # check if passwords match
                if sha256_crypt.verify(data["password"], member["password"]):
                    token = jwt.encode(
                        {
                            'uid':member["id"],
                            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
                        }, app.config['SECRET_KEY'])

                    return jsonify({"success":True, "token":token.decode('UTF-8')}), 200

                return jsonify({"success":False, "message":"Incorrect username or password"}), 400

            return jsonify({"success":False, "message":"User not found"}), 400
        return jsonify(result), 400

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

            user_object = {
                "email" : data["email"],
                "password" : sha256_crypt.encrypt(str(data["password"]))
            }

            return User.reset_password(user_object)
        return jsonify(result), 400

    @staticmethod
    def get_user(user_id):
        """ return a passed user using the user id passed """
        return User.get_user(user_id)

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
            result = User.get_user(current_user)
            if result["success"]:
                if result["user"]["email"] == data["email"]:
                    return True
            return False
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
