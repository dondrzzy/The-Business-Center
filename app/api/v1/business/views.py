""" business routes """
from flask import request, jsonify, Blueprint
from app import is_logged_in
from app.services.business_service import BusinessService
BS = BusinessService()

#config
BUSINESS_BLUEPRINT = Blueprint(
    'business', __name__
)

# register a business
@BUSINESS_BLUEPRINT.route('/api/v1/businesses', methods=['POST'])
@is_logged_in
def register_business(current_user):
    """ register a business route """
    business = request.get_json()

    result = BS.register_business(int(current_user), business)

    return result


# get all businesses
@BUSINESS_BLUEPRINT.route('/api/v1/businesses')
def get_all_businesses():
    """ get all businesses route """
    return jsonify({"success":True, "businesses":BS.get_all_businesses()["businesses"]}), 200

# get single business businesses
@BUSINESS_BLUEPRINT.route('/api/v1/businesses/<business_id>')
def get_business(business_id):
    """ get a business route """
    return jsonify(BS.get_business(business_id))


@BUSINESS_BLUEPRINT.route('/api/v1/businesses/<business_id>', methods=['PUT'])
@is_logged_in
def update_business(current_user, business_id):
    """update a business route """
    data = request.get_json()

    return BS.update_business(current_user, business_id, data)


@BUSINESS_BLUEPRINT.route('/api/v1/businesses/<business_id>', methods=['DELETE'])
@is_logged_in
def delete_business(current_user, business_id):
    """ delete a business route"""
    return BS.delete_business(business_id, current_user)
