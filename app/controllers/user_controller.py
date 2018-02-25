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
        fields = ['name', 'email', 'password', 'password_c']
        res = self.check_req_fields(data, fields, True)
        if res["success"]:
            user_obj = {
                "name" : data["name"], "email" : data["email"],
                "password" : data["password"]
            }
            return UM.register_user(user_obj)
        return res

    # login user
    def login_user(self, data):
        """login_user"""
        fields = ['email', 'password']
        res = self.check_req_fields(data, fields)
        if res["success"]:
            user_obj = {
                "email" : data["email"], "password" : data["password"]
            }
            if "email" in session and session["email"] == data["email"]:
                return {"success":False, "msg":"Already logged in. Redirecting..."}
            return UM.login_user(user_obj)
        return res

    # reset password
    def reset_password(self, data):
        """reset_password"""
        fields = ['email', 'password', 'password_c']
        res = self.check_req_fields(data, fields, True)
        if res["success"]:
            user_obj = {
                "email" : data["email"], "password" : (data["password"])
            }
            return UM.reset_password(user_obj)
        return res

    def check_req_fields(self, obj, fields, comp_pwds=False):
        """checks required fields"""
        for field in fields:
            if field not in obj:
                return {"success":False, "msg":field + " is required"}
        if comp_pwds:
            if obj["password"] != obj["password_c"]:
                return {"success":False, "msg":"passwords do not match"}
        return {"success":True}
