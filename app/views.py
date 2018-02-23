""" routes file """
from flask import request, jsonify, session

from app import app

# import controllers
from app.controllers.user_controller import UserController
from app.controllers.business_controller import BusinessController
from app.controllers.review_controller import ReviewController


# instantiate controllers
UC = UserController()
BC = BusinessController()
RC = ReviewController()



# routes
@app.route('/', methods=["GET"])
def index():
    """defualt route"""
    return jsonify({"user":"Hello there"})

# register user
@app.route('/api/v1/auth/register', methods=['POST'])
def register_user():
    """registers user"""
    data = request.get_json()

    # pass data to the user controller
    return jsonify(UC.register_user(data))


# login user
@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    """logs in user"""
    data = request.get_json()

    # submit data to user controller
    return jsonify(UC.login_user(data))


# logout user
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """logs out user."""
    session.clear()
    return jsonify({"success":True, "msg":"You are logged out"})

# reset user password
@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """resets password"""
    data = request.get_json()

    # send data to the user controller
    return jsonify(UC.reset_password(data))


# Business routes
@app.route('/api/v1/businesses', methods=['POST'])
def register_business():
    """register business"""
    # user must be signed in
    if "id" not in session:
        return jsonify({"success":False, "msg":"Access denied! Login"})
    data = request.get_json()

    return jsonify(BC.register_business(data))


@app.route('/api/v1/businesses')
def get_all_businesses():
    """get all businesses."""
    return jsonify(BC.get_all_businesses())


# get a specific business
@app.route('/api/v1/businesses/<businessId>')
def get_business(businessId):
    """get business"""
    return jsonify(BC.get_business(businessId))

# update business
@app.route('/api/v1/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
    """Update Business"""
    if "id" not in session:
        return jsonify({"success":False, "msg":"Access denied! Login"})

    data = request.get_json()

    return jsonify(BC.update_business(businessId, data))

# delete business
@app.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    """delete business"""
    if "id" not in session:
        return jsonify({"success":False, "msg":"Access denied! Login"})

    return jsonify(BC.delete_business(businessId))


# Reviews
@app.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
def add_review(businessId):
    """add review to business"""
    if "id" not in session:
        return jsonify({"success":False, "msg":"Access denied! Login"})

    data = request.get_json()

    return jsonify(RC.add_review(data, businessId))


@app.route('/api/v1/businesses/<businessId>/reviews')
def get_business_reviews(businessId):
    """get business review"""
    return jsonify(RC.get_business_reviews(businessId))
