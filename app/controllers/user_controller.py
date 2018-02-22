from passlib.hash import sha256_crypt
from app.models.user import UserModel
import pprint
import jwt
import datetime
from app import app
UserModel = UserModel()

class UserController(object):
    """docstring for UserController"""
    def __init__(self, argz = 0):
        self.argz = argz

    def register_user(self, data):
        if "name" not in data:
            return {"success":False, "msg":"name is required"}
        elif "email" not in data:
            return {"success":False, "msg":"email is required"}
        elif "password" not in data:
            return {"success":False, "msg":"password is required"}
        elif "password_c" not in data:
            return {"success":False, "msg":"password_c is required"}
        elif data["password"] != data["password_c"]:
            return {"success":False, "msg":"passwords do not match"}

        user_obj = {
            "name" : data["name"],
            "email" : data["email"],
            "password" : data["password"]
        }
        # check if email exists
        if UserModel.email_exists(user_obj["email"])["success"]:
            return {"success":False, "msg":"Email already exists"}

        # create user
        UserModel.register(user_obj)
        return {"success":True, "msg":"Account created successfully"}

    # login user
    def login_user(self, data):
        if "email" not in data:
            return {"success":False, "msg":"email is required"}
        if "password" not in data:
            return {"success":False, "msg":"password is required"}

        user_obj = {
            "email" : data["email"],
            "password" : data["password"]
        }

        # check if email exists in the db
        res = UserModel.is_member(user_obj)

        if res["success"]:
            member = res["user"]
            # check if passwords match
            if sha256_crypt.verify(user_obj["password"], member["password"]):
                token = jwt.encode({'uid':member["id"], 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
                
                return {"success":True, "token":token.decode('UTF-8')}

            return { "success":False, "message":"Incorrect username or password" }

        return {"success":False, "message":"User not found"}

    # reset password
    def reset_password(self, data):
        if "email" not in data:
            return {"success":False, "msg":"email is required"}
        elif "password" not in data:
            return {"success":False, "msg":"password is required"}
        elif "password_c" not in data:
            return {"success":False, "msg":"password_c is required"}
        elif data["password"] != data["password_c"]:
            return {"success":False, "msg":"passwords do not match"}

        user_obj = {
            "email" : data["email"],
            "password" : sha256_crypt.encrypt(str(data["password"]))
        }

        return UserModel.reset_password(user_obj)

    def get_user(self, uid):
        return UserModel.get_user(uid)
        
    