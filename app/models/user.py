""" docstring for User model"""
from passlib.hash import sha256_crypt # For hashing password
from app import db
from app import jsonify
# from app.model import User

class User(db.Model):
    """ Define a 'User' model mapped to table 'user' """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def verify_password(self, in_password):
        """Verify the given password with the stored password hash"""
        return sha256_crypt.verify(in_password, self.pwhash)

    def register(self):
        """add user to db"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_user(user_id):
        """ get user from db """
        user = User.query.filter_by(id=user_id).first()
        member = {
            'id':user.id,
            'name':user.name,
            'email':user.email
        }
        return {"success":True, "user":member}

    @staticmethod
    def email_exists(email):
        """ check if email exists in db """
        user = User.query.filter_by(email=email).first()
        if not user:
            return{"success":False}
        return {"success":True}


    @staticmethod
    def is_member(_user):
        """ check if email exists in db """
        user = User.query.filter_by(email=_user["email"]).first()
        if not user:
            return {"success":False}

        member = {
            'id':user.id,
            'email':user.email,
            'password':user.password
        }
        return {"success":True, "user":member}

    @staticmethod
    def reset_password(_user):
        """ docstsing for resetting db password """
        user = User.query.filter_by(email=_user["email"]).first()
        if not user:
            return jsonify({"success":False, "message":"User not found"})
        user.password = _user["password"]
        db.session.commit()
        return jsonify({"success":True, "message":"Password reset successfully"}), 200
