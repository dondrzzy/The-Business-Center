""" docstring for my shcemas """
from passlib.hash import sha256_crypt # For hashing password
from app import db



class User(db.Model):
    """ Define a 'User' model mapped to table 'user' """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, name, email, password):
        """Constructor: to hash password"""
        self.password = sha256_crypt.encrypt(str(password))  # hash submitted password
        self.name = name
        self.email = email

    def verify_password(self, in_password):
        """Verify the given password with the stored password hash"""
        return sha256_crypt.verify(in_password, self.pwhash)

class Business(db.Model):
    """ create Business schema """
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(80), nullable=False)

    def __init__(self, uid, name, category, location):
        self.name = name
        self.category = category
        self.location = location
        self.uid = uid

class Review(db.Model):
    """ create reviews schema """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    bid = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)

    def __init__(self, text, bid, uid):
        self.text = text
        self.bid = bid
        self.uid = uid
