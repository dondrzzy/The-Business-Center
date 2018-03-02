""" docstring for initial app settings """
import os
from flask import Flask, request, jsonify
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from app.config import CONF
import jwt
from flasgger import Swagger
from app.apidocs import Apidocs


# Flask-SQLAlchemy: Initialize
app = Flask(__name__)
app.config['SWAGGER'] = Apidocs.swagger_conf
swagger = Swagger(app)

#Configuration Parameters for the app environment
ENV = os.getenv("ENVIRON", 'testing')
app.config.from_object(CONF['production'])

db = SQLAlchemy(app)

from app.services.token_service import TokenService
# instantiate the service
TS = TokenService()

# create an auth decorator
def is_logged_in(f):
    """ check if logged in """
    @wraps(f)
    def decorated(*args, **kwargs):
        """ docstring for check token decorator """
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'success':False, 'token':False, 'message':'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = data["uid"]
        except:
            return jsonify({'success':False, 'token':False, 'message':'Token is invalid'}), 401
        response = TS.is_blacklisted(token)
        if response["success"]:
            return jsonify({'success':False, 'token':False, 'message':'Token is invalid, Please login'}), 401
        return f(current_user, *args, **kwargs)

    return decorated

# import blueprints
from app.api.v1.users.views import users_blueprint
from app.api.v1.business.views import business_blueprint
from app.api.v1.review.views import review_blueprint

# registerblueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(business_blueprint)
app.register_blueprint(review_blueprint)
