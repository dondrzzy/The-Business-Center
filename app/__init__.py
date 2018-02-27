""" docstring for initial app settings """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import app_configuration

# Flask-SQLAlchemy: Initialize
app = Flask(__name__)

#Configuration Parameters for the app
environ = os.getenv("ENVIRON", 'development')
app.config.from_object(app_configuration[environ])

db = SQLAlchemy(app)

from app.schemas import User, Business, Review

with app.app_context():
    db.create_all()

from . import views
