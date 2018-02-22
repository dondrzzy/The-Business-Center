from flask import request, jsonify, render_template, url_for, session
import pprint
from functools import wraps
import jwt
from app import app
from app.controllers.user_controller import UserController
from app.controllers.business_controller import BusinessController
from app.controllers.review_controller import ReviewController

UserController = UserController()
BusinessController = BusinessController()
ReviewController = ReviewController()


# Front end routes
# splash page
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# register route
@app.route('/register')
def load_register():
    return render_template('register_user.html')

@app.route('/login')
def load_login():
    return render_template('login.html')

@app.route('/reset-password')
def load_reset_password():
    return render_template('/reset-password')
# \register business
@app.route('/register_business')
def load_register_business():
    return render_template('/register_business.html')

# load my  businesses
@app.route('/dashboard')
def load_dashboard():
    return render_template('/dashboard.html')

# get all businesses
@app.route('/businesses')
def load_businesses():
    return render_template('/businesses.html')

# get single business
@app.route('/businesses/<businessId>')
def load_business(businessId):
    return render_template('business.html', id = businessId)


# edit a business--- ajax

# search for businesses



# API routes routes

@app.route('/api/v1/auth/register', methods=['POST'])
def register():

    data = request.get_json()

    res = UserController.register_user(data)
    
    return jsonify(res)


@app.route('/api/v1/auth/login', methods=['POST'])
def login():

    data = request.get_json()

    res = UserController.login_user(data)

    return jsonify(res)

def is_logged_in(f):
    @wraps(f)
    def decorated(*args, **kwargs):
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
    session.clear()
    return jsonify({"success":True, "msg":"You are logged out"})

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    return jsonify(UserController.reset_password(data))

# register a business
@app.route('/api/v1/businesses', methods=['POST'])
@is_logged_in
def register_business(current_user):
    
    business = request.get_json()

    res = BusinessController.register_business(int(current_user), business)

    return jsonify(res)


# get all businesses
@app.route('/api/v1/businesses')
def get_all_businesses():
    return jsonify({"success":True, "businesses":BusinessController.get_all_businesses()["businesses"]})

# get single business businesses
@app.route('/api/v1/businesses/<businessId>')
def get_business(businessId):
    return jsonify(BusinessController.get_business(businessId))

# incomplete
@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
@is_logged_in
def update_business(current_user, businessId):
    data = request.get_json()

    return jsonify(BusinessController.update_business(current_user, businessId, data))
    


@app.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
@is_logged_in
def delete_business(current_user, businessId):
    return jsonify(BusinessController.delete_business(businessId, current_user))
    




# Reviews routes
@app.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@is_logged_in
def add_review(current_user, businessId):
    
    data = request.get_json()
    return jsonify(ReviewController.add_review(data, businessId, current_user))

# get specific review
@app.route('/api/v1/businesses/<businessId>/reviews')
def get_business_reviews(businessId):
    return jsonify(ReviewController.get_business_reviews(businessId))

