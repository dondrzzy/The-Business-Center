""" docstring for review controller """
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
        if not business_id.isdigit():
            return {"success":False, "message":"Invalid business id"}

        if "text" not in data:
            return {"success":False, "message":"Provide a review ('text')"}

        review = {
            "text" : data["text"]
        }

        # check if business id exists
        business_result = BS.get_business(business_id)
        if not business_result["success"]:
            return {"success":False, "message":"Business with id "+business_id+" not found"}

        Review(text=data["text"], business_id=business_id, user_id=user_id).add_review()

        return {"success":True, "message":"Review posted successfully"}

    def get_business_reviews(self, business_id):
        """ get a business reviews """
        return Review.get_business_reviews(business_id)
        