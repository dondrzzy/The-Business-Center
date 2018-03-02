
from flask import request, Blueprint
from app import is_logged_in
from app.services.review_service import ReviewService
RS = ReviewService()

#config
review_blueprint = Blueprint(
    'review', __name__
)

# Reviews routes
@review_blueprint.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@is_logged_in
def add_review(current_user, businessId):
    """ adds a review route """
    data = request.get_json()
    return RS.add_review(data, businessId, current_user)

# get specific review
@review_blueprint.route('/api/v1/businesses/<businessId>/reviews')
def get_business_reviews(businessId):
    """ get business rev route """
    return RS.get_business_reviews(businessId)