""" all decorated functions defined here """
from functools import wraps
import jwt
from flask import request, jsonify
from app  import app
from app.services.token_service import TokenService

# instantiate the service
TS = TokenService()

# create an auth decorator
def is_logged_in(func):
    """ check if logged in """
    @wraps(func)
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
        return func(current_user, *args, **kwargs)

    return decorated

def valid_business_id(func):
    """
    decorator to check if a valid business id is passed
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        """ check business id in request arguments """
        business_id = request.view_args['business_id']
        try:
            int(business_id)
        except ValueError:
            return jsonify({'success':False, 'message':'Invalid business Id'}), 400
        return func(*args, **kwargs)

    return decorated
