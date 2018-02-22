from app import db
from app.schemas import User


class UserModel(object):
    """docstring for User"""
    def __init__(self, users = []):
        self.users = users


    def register(self, user):
        new_user = User(user["name"], user["email"], user["password"])
        db.session.add(new_user)
        db.session.commit()
        
    def get_user(self, uid):
        user = User.query.filter_by(id=uid).first()
        member = {
            'id':user.id,
            'name':user.name,
            'email':user.email
        }
        return {"success":True, "user":member}

    def login(self, _user):
        for user in self.users:
            if user["email"] == _user["email"]:
                if user["password"] == _user["password"]:
                    # session["id"] = user["id"]
                    return {"success":True, "pwd":True}
                return {"success":True, "pwd":False}

        return {"success":False, "pwd":False}

    def email_exists(self, email):
        user = User.query.filter_by(email=email).first()
        if not user:
            return{"success":False}
        return {"success":True}
        

    def is_member(self, _user):
        user = User.query.filter_by(email=_user["email"]).first()
        if not user:
            return {"success":False}

        member = {
            'id':user.id,
            'email':user.email,
            'password':user.password
        }
        return {"success":True, "user":member}

    def reset_password(self, _user):
        user = User.query.filter_by(email=_user["email"]).first()
        if not user:
            return {"success":False, "msg":"User not  found"}
        user.password = _user["password"]
        db.session.commit()
        return {"success":True, "msg":"Password reset successfully"}



