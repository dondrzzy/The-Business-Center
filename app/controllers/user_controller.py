""" User Class"""
from flask import session
from app.models.user import UserModel

# instatiate model
UM = UserModel()

class UserController(object):
    """docstring for UserController"""
    def __init__(self, argz=0):
        self.argz = argz

    def register_user(self, data):
        """register_user"""

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

        return UM.register_user(user_obj)

    # login user
    def login_user(self, data):
        """login_user"""
        if "email" not in data:
            return {"success":False, "msg":"Email is required"}
        if "password" not in data:
            return {"success":False, "msg":"Password is required"}

        user_obj = {
            "email" : data["email"],
            "password" : data["password"]
        }


        # check if already logged in user
        if "email" in session and session["email"] == data["email"]:
            return {"success":False, "msg":"Already logged in. Redirecting..."}

        return UM.login_user(user_obj)

    # reset password
    def reset_password(self, data):
        """reset_password"""
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

            "password" : (data["password"])
        }

        return UM.reset_password(user_obj)
