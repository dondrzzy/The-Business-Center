""" docstring for review controller """
from app.models.review import ReviewModel
from app.controllers.business_controller import BusinessController

# instantiate models
BC = BusinessController()
RM = ReviewModel()

class ReviewController(object):
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
        b_res = BC.get_business(bid)
        if not b_res["success"]:
            return {"success":False, "msg":"Business with id "+bid+" not found"}

        RM.add_review(review, bid, uid)

        return {"success":True, "msg":"Review posted successfully"}

    def get_business_reviews(self, bid):
        """ get a business reviews """
        return RM.get_business_reviews(bid)
        