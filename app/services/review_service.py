""" docstring for review controller """
from app.models.review import ReviewModel
from app.services.business_service import BusinessService

# instantiate models
BS = BusinessService()
RM = ReviewModel()

class ReviewService(object):
    """docstring for ReviewController"""
    def __init__(self, arg=0):
        self.arg = arg

    def add_review(self, data, bid, uid):
        """ add a review to a business """
        if not bid.isdigit():
            return {"success":False, "msg":"Invalid business id"}

        if "text" not in data:
            return {"success":False, "msg":"Provide a review ('text')"}

        review = {
            "text" : data["text"]
        }

        # check if bid exists
        b_res = BS.get_business(bid)
        if not b_res["success"]:
            return {"success":False, "msg":"Business with id "+bid+" not found"}

        RM.add_review(review, bid, uid)

        return {"success":True, "msg":"Review posted successfully"}

    def get_business_reviews(self, bid):
        """ get a business reviews """
        return RM.get_business_reviews(bid)
        