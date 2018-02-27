""" docstring for initial app settings """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import CONF

# Flask-SQLAlchemy: Initialize
app = Flask(__name__)

#Configuration Parameters for the app
ENV = os.getenv("ENVIRON", 'testing')
app.config.from_object(CONF[ENV])

db = SQLAlchemy(app)

from app.schemas import User, Business, Review

with app.app_context():
    db.create_all()

from . import views
