from passlib.hash import sha256_crypt # For hashing password
from app import db



# Define a 'Base' model for other database tables to inherit
class Base(db.Model):
   __abstract__  = True
   date_created  = db.Column(db.DateTime,
         default=db.func.current_timestamp())
   date_modified = db.Column(db.DateTime,
         default=db.func.current_timestamp(),
         onupdate=db.func.current_timestamp())

# Define a 'User' model mapped to table 'user'
class User(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    bid = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)

    def __init__(self, text, bid, uid):
      self.text = text
      self.bid = bid
      self.uid = uid


