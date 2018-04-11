""" docstring for review controller """
import re
from flask import jsonify
from app.services.business_service import BusinessService
from app.models.review import Review

# instantiate models
BS = BusinessService()

class ReviewService(object):
    """docstring for ReviewController"""
    def __init__(self, arg=0):
        self.arg = arg


    def add_review(self, data, business_id, user_id):
        """ add a review to a business """

        if "text" not in data:
            return jsonify({"success":False, "message":"Provide a review ('text')"}), 400

        # check if a valid business review was sent
        valid_review_res = self.validate_reviews_input(data)
        if valid_review_res["success"]:
            # check if business id exists
            business_result = BS.check_business(business_id)
            if not business_result["success"]:
                return jsonify({"success":False,
                                "message":"Business with id "+business_id+" not found"}), 404

            Review(text=data["text"], business_id=business_id, user_id=user_id).add_review()

            return jsonify({"success":True, "message":"Review posted successfully"}), 201
        return jsonify(valid_review_res)

    @staticmethod
    def get_business_reviews(business_id):
        """ get a business reviews """
        res = Review.get_business_reviews(business_id)
        if res["success"]:
            return jsonify(res), 200
        return jsonify(res), 404

    def validate_reviews_input(self, data):
        """ vaidate business input for empty and invalid fields """
        if 'text' in data:
            if not bool(re.fullmatch('^[a-zA-Z0-9]{2,25}(?!\s*$).+', data["text"])):
                return { "success":False, "message":"Invalid business review"}

        return {"success":True}
        