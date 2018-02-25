"""docstring for User Model"""
from flask import session

class UserModel(object):
    """docstring for User"""
    inituser = {"id":1, "name":"Sibo", "email":"test@gmail.com", "password":"1234"}
    def __init__(self, users=[inituser]):
        self.users = users

    # add user to the users array
    def register_user(self, _user):
        """docstring for register_user method"""
        for user in self.users:
            if _user["email"] == user["email"]:
                return {"success":False, "msg":"Email already exists,try another one."}

        new_user = {
            "id" : len(self.users)+1,
            "name" : _user["name"],
            "email" : _user["email"],
            "password" : _user["password"]
        }
        self.users.append(new_user)
        return {"success":True, "msg":"Account created successfully", "users":self.users}

    # Add user to session
    def login_user(self, _user):
        """docstring for login_user method"""
        for user in self.users:
            if user["email"] == _user["email"]:
                if user["password"] == _user["password"]:
                    session["id"] = user["id"]
                    session['logged_in'] = True
                    session['email'] = user['email']
                    return {"success":True, "msg":"User logged in successfully"}
                return {"success":True, "msg":"Email and Password mismatch"}
        return {"success":False, "msg":"User not found, Please register"}

    def get_users(self):
        """docstring for get_users method"""
        return self.users

    def no_users(self):
        """docstring for no_users method"""
        return len(self.users)

    def reset_password(self, _user):
        """docstring for reset_password method"""
        for user in self.users:
            if _user["email"] == user["email"]:
                user["password"] = _user["password"]
                return {"success":True, "msg":"Password reset successfully"}
        return {"success":False, "msg":"User not found"}
