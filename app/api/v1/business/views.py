
from flask import request, jsonify, render_template, session, redirect, url_for, Blueprint
from app import is_logged_in
from app.services.business_service import BusinessService
BS = BusinessService()

#config
business_blueprint = Blueprint(
    'business', __name__
)

# register a business
@business_blueprint.route('/api/v1/businesses', methods=['POST'])
@is_logged_in
def register_business(current_user):
    """ register a business route """
    business = request.get_json()

    result = BS.register_business(int(current_user), business)

    return jsonify(result)


# get all businesses
@business_blueprint.route('/api/v1/businesses')
def get_all_businesses():
    """ get all businesses route """
    return jsonify({"success":True, "businesses":BS.get_all_businesses()["businesses"]})

# get single business businesses
@business_blueprint.route('/api/v1/businesses/<businessId>')
def get_business(businessId):
    """ get a business route """
    return jsonify(BS.get_business(businessId))

# incomplete
@business_blueprint.route('/api/v1/businesses/<businessId>', methods=['PUT'])
@is_logged_in
def update_business(current_user, businessId):
    """update a business route """
    data = request.get_json()

    return jsonify(BS.update_business(current_user, businessId, data))



@business_blueprint.route('/api/v1/businesses/<businessId>', methods=['DELETE'])
@is_logged_in
def delete_business(current_user, businessId):
    """ delete a business route"""
    return jsonify(BS.delete_business(businessId, current_user))