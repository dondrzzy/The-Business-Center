""" business routes """
from flask import request, jsonify, Blueprint
from app import app
from app.services.decorator_services import is_logged_in, valid_business_id
from app.services.business_service import BusinessService
BS = BusinessService()

#config
BUSINESS_BLUEPRINT = Blueprint(
    'business', __name__
)

# register a business
@BUSINESS_BLUEPRINT.route('/businesses', methods=['POST'])
@is_logged_in
def register_business(current_user):
    """ register a business route """
    business = request.get_json()

    result = BS.register_business(int(current_user), business)

    return result


# get all businesses
# @BUSINESS_BLUEPRINT.route('/businesses')
# def get_all_businesses():
#     """ get all businesses route """
#     return jsonify({"success":True, "businesses":BS.get_all_businesses()["businesses"]}, ), 200

# paginate through businesses
@BUSINESS_BLUEPRINT.route('/businesses')
def get_businesses():
    """
    get businesses, search by name, filter by location, categoory
    paginate result
    """
    search_string = request.args.get('q', None)
    location = request.args.get('location', None)
    category = request.args.get('category', None)

    # get page nuumber
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', app.config["BUSINESSES_PER_PAGE"], type=int)

    return jsonify(BS.get_businesses(page, limit, search_string, location, category)), 200

# get single business businesses
@BUSINESS_BLUEPRINT.route('/businesses/<business_id>')
@valid_business_id
def get_business(business_id):
    """ get a business route """
    return jsonify(BS.get_business(business_id))


@BUSINESS_BLUEPRINT.route('/businesses/<business_id>', methods=['PUT'])
@valid_business_id
@is_logged_in
def update_business(current_user, business_id):
    """update a business route """
    data = request.get_json()

    return BS.update_business(current_user, business_id, data)


@BUSINESS_BLUEPRINT.route('/businesses/<business_id>', methods=['DELETE'])
@valid_business_id
@is_logged_in
def delete_business(current_user, business_id):
    """ delete a business route"""
    return BS.delete_business(business_id, current_user)
