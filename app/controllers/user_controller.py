""" docstring for user controller"""
import datetime
import jwt
from passlib.hash import sha256_crypt
from app import app
from app.models.user import UserModel

# instatiate models
UM = UserModel()

class UserController(object):
    """docstring for UserController"""
    def __init__(self, argz=0):
        self.argz = argz

    def register_user(self, data):
        """docstring for registering a  user account """
        fields = ['name', 'email', 'password', 'password_c']
        res = self.check_req_fields(data, fields, True)
        if res["success"]:

            user_obj = {
                "name" : data["name"],
                "email" : data["email"],
                "password" : data["password"]
            }
            # check if email exists
            if UM.email_exists(user_obj["email"])["success"]:
                return {"success":False, "msg":"Email already exists"}

            # create user
            UM.register(user_obj)
            return {"success":True, "msg":"Account created successfully"}
        return res

    # login user
    def login_user(self, data):
        """ login in user """
        fields = ['email', 'password']
        res = self.check_req_fields(data, fields)
        if res["success"]:

            user_obj = {
                "email" : data["email"],
                "password" : data["password"]
            }

            # check if email exists in the db
            res = UM.is_member(user_obj)

            if res["success"]:
                member = res["user"]
                # check if passwords match
                if sha256_crypt.verify(user_obj["password"], member["password"]):
                    token = jwt.encode(
                        {
                            'uid':member["id"],
                            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
                        }, app.config['SECRET_KEY'])

                    return {"success":True, "token":token.decode('UTF-8')}

                return {"success":False, "message":"Incorrect username or password"}

            return {"success":False, "message":"User not found"}
        return res

    # reset password
    def reset_password(self, data):
        """ docstring for reset a password """
        fields = ['email', 'password', 'password_c']
        res = self.check_req_fields(data, fields, True)
        if res["success"]:

            user_obj = {
                "email" : data["email"],
                "password" : sha256_crypt.encrypt(str(data["password"]))
            }

            return UM.reset_password(user_obj)
        return res

    def get_user(self, uid):
        """ return a passed user """
        return UM.get_user(uid)

    def check_req_fields(self, obj, fields, comp_pwds=False):
        """checks required fields"""
        for field in fields:
            if field not in obj:
                return {"success":False, "msg":field + " is required"}
        if comp_pwds:
            if obj["password"] != obj["password_c"]:
                return {"success":False, "msg":"passwords do not match"}
        return {"success":True}
