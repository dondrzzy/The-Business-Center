""" routes for the reviews model """
from flask import request, Blueprint
from app.services.decorator_services import is_logged_in, valid_business_id
from app.services.review_service import ReviewService
RS = ReviewService()

#config
REVIEWS_BLUEPRINT = Blueprint(
    'review', __name__
)

# Reviews routes
@REVIEWS_BLUEPRINT.route('/businesses/<business_id>/reviews', methods=['POST'])
@valid_business_id
@is_logged_in
def add_review(current_user, business_id):
    """ adds a review route """
    data = request.get_json()
    return RS.add_review(data, business_id, current_user)

# get specific review
@REVIEWS_BLUEPRINT.route('/businesses/<business_id>/reviews')
@valid_business_id
def get_business_reviews(business_id):
    """ get business rev route """
    return RS.get_business_reviews(business_id)
