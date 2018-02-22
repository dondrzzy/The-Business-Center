from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemy: Initialize
app = Flask(__name__)

#Configuration Parameters for the app
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:engneerdon@localhost/tbc_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
db = SQLAlchemy(app)

from app.schemas import User, Business, Review

with app.app_context():
	db.create_all()


from . import views
