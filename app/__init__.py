""" docstring for initial app settings """
import os
from functools import wraps
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
            return jsonify({'success':False, 'token':False,
                            'message':'Token is invalid, Please login'}), 401
        return f(current_user, *args, **kwargs)

    return decorated

# import blueprints
from app.api.v1.users.views import USERS_BLUEPRINT
from app.api.v1.business.views import BUSINESS_BLUEPRINT
from app.api.v1.review.views import REVIEWS_BLUEPRINT

# registerblueprints
app.register_blueprint(USERS_BLUEPRINT)
app.register_blueprint(BUSINESS_BLUEPRINT)
app.register_blueprint(REVIEWS_BLUEPRINT)
