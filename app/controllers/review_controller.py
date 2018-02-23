""" Review Model """
from app.models.review import ReviewModel
RM = ReviewModel()

class ReviewController(object):
    """docstring for ReviewController"""
    def __init__(self, arg=0):
        self.arg = arg

    def add_review(self, data, bid):
        """ add_review """
        # check passed business id
        if not bid.isdigit():
            return {"success":False, "msg":"Invalid business id"}

        # verify text
        if "text" not in data:
            return {"success":False, "msg":"Provide a review ('text')"}

        review = {
            "text" : data["text"]
        }

        return RM.add_review(review, bid)

    def get_business_reviews(self, bid):
        """ get_business_reviews """
        if bid.isdigit():
            return RM.get_business_reviews(bid)
        return {"success":False, "msg":"Invalid business id"}
 