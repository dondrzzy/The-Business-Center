""" docstring for review controller """
from flask import jsonify
from app.services.business_service import BusinessService
from app.models.review import Review

# instantiate models
BS = BusinessService()

class ReviewService(object):
    """docstring for ReviewController"""
    def __init__(self, arg=0):
        self.arg = arg

    @staticmethod
    def add_review(data, business_id, user_id):
        """ add a review to a business """

        if "text" not in data:
            return jsonify({"success":False, "message":"Provide a review ('text')"}), 422



        # check if business id exists
        business_result = BS.check_business(business_id)
        if not business_result:
            return jsonify({"success":False,
                            "message":"Business with id "+business_id+" not found"}), 404

        Review(text=data["text"], business_id=business_id, user_id=user_id).add_review()

        return jsonify({"success":True, "message":"Review posted successfully"}), 201


    @staticmethod
    def get_business_reviews(business_id):
        """ get a business reviews """
        reviews = Review.get_business_reviews(business_id)
        if not reviews:
            return jsonify({"success":False, "msg":"No Business Reviews"}), 404
        output = []
        for review in reviews:
            review_object = {
                'id':review.id,
                'text':review.text,
                'user':review.user.name
            }
            output.append(review_object)
        return jsonify({"success":True, "reviews":output}), 200
        