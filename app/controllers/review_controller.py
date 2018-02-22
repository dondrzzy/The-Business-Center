from app.models.review import ReviewModel
from app.controllers.business_controller import BusinessController
from app.controllers.user_controller import UserController
BusinessController = BusinessController()
UserController = UserController()
ReviewModel = ReviewModel()

class ReviewController(object):
    """docstring for ReviewController"""
    def __init__(self, arg=0):
        self.arg = arg

    def add_review(self, data, bid, uid):
        if not bid.isdigit():
            return {"success":False, "msg":"Invalid business id"}

        if "text" not in data:
            return {"success":False, "msg":"Provide a review ('text')"}

        review = {
            "text" : data["text"]
        }

        # check if bid exists
        b_res = BusinessController.get_business(bid)
        if not b_res["success"]:
            return {"success":False, "msg":"Business with id "+bid+" not found"}

        ReviewModel.add_review(review, bid, uid)

        return {"success":True, "msg":"Review posted successfully"}

    def get_business_reviews(self, bid):
        return ReviewModel.get_business_reviews(bid)
        