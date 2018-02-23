""" initial setting for app"""
import os
import sys
from flask import Flask

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'


from . import views
