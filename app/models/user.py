""" docstring for User model"""
from passlib.hash import sha256_crypt # For hashing password
from app import db
# from app.model import User

class User(db.Model):
    """ Define a 'User' model mapped to table 'user' """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    reset_token = db.Column(db.String(400), nullable=True)


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
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def email_exists(user):
        """ check if email exists in db """
        return User.query.filter_by(email=user["email"]).first()


    @staticmethod
    def reset_password(user):
        """ docstsing for resetting db password """
        registered_user = User.query.filter_by(email=user["email"]).first()
        registered_user.password = user["password"]
        db.session.commit()

    def save_reset_token(self, token):
        """ save password reset token """
        self.reset_token = token
        db.session.commit()

    @staticmethod
    def get_token_user(id, token):
        return User.query.filter_by(id=id, reset_token=token).first()
