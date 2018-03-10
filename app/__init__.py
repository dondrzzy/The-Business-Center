""" docstring for initial app settings """
import os
import jwt
from flasgger import Swagger
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.apidocs import Apidocs
from app.config import CONF


# Flask-SQLAlchemy: Initialize
app = Flask(__name__)
app.config['SWAGGER'] = Apidocs.swagger_conf
swagger = Swagger(app)

#Configuration Parameters for the app environment
ENV = os.getenv("ENVIRON", 'testing')
app.config.from_object(CONF[ENV])

db = SQLAlchemy(app)

# import application error views
from app.api.v1 import error_views

# import blueprints
from app.api.v1.users.views import USERS_BLUEPRINT
from app.api.v1.business.views import BUSINESS_BLUEPRINT
from app.api.v1.review.views import REVIEWS_BLUEPRINT

# registerblueprints
app.register_blueprint(USERS_BLUEPRINT, url_prefix='/api/v1/auth')
app.register_blueprint(BUSINESS_BLUEPRINT, url_prefix='/api/v1')
app.register_blueprint(REVIEWS_BLUEPRINT, url_prefix='/api/v1')
