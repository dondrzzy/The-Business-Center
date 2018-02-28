""" docstring for my routes """
from functools import wraps
from flask import request, jsonify, render_template, session
import jwt
from app import app
from app.services.user_service import UserService
from app.services.business_service import BusinessService
from app.services.review_service import ReviewService

US = UserService()
BS = BusinessService()
RS = ReviewService()


# Front end routes
# splash page
@app.route('/', methods=["GET"])
def index():
    """ splash page template """
    return render_template('index.html')



# API routes routes

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """" register a user route """
    data = request.get_json()

    res = US.register_user(data)

    return jsonify(res)

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """login route """
    data = request.get_json()

    res = US.login_user(data)

    return jsonify(res)

def is_logged_in(f):
    """ check if logged in """
    @wraps(f)
    def decorated(*args, **kwargs):
        """ docstring for checktoken decorator """
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
        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ logout route """
    session.clear()
    return jsonify({"success":True, "msg":"You are logged out"})

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ reset a password """
    data = request.get_json()
    return jsonify(US.reset_password(data))

# register a business
@app.route('/api/v1/businesses', methods=['POST'])
@is_logged_in
def register_business(current_user):
    """ register a business route """
    business = request.get_json()

    res = BS.register_business(int(current_user), business)

    return jsonify(res)


# get all businesses
@app.route('/api/v1/businesses')
def get_all_businesses():
    """ get all businesses route """
    return jsonify({"success":True, "businesses":BS.get_all_businesses()["businesses"]})

# get single business businesses
@app.route('/api/v1/businesses/<businessId>')
def get_business(businessId):
    """ get a business route """
    return jsonify(BS.get_business(businessId))

# incomplete
@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
@is_logged_in
def update_business(current_user, businessId):
    """update a business route """
    data = request.get_json()

    return jsonify(BS.update_business(current_user, businessId, data))



@app.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
@is_logged_in
def delete_business(current_user, businessId):
    """ delete a business route"""
    return jsonify(BS.delete_business(businessId, current_user))


# Reviews routes
@app.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@is_logged_in
def add_review(current_user, businessId):
    """ adds a review route """
    data = request.get_json()
    return jsonify(RS.add_review(data, businessId, current_user))

# get specific review
@app.route('/api/v1/businesses/<businessId>/reviews')
def get_business_reviews(businessId):
    """ get business rev route """
    return jsonify(RS.get_business_reviews(businessId))
