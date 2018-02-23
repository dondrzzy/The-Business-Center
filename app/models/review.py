"""docstring for Review Model"""
from flask import session

class ReviewModel(object):
    """docstring for Revuew"""

    def __init__(self, reviews=[]):
        self.reviews = reviews

    def add_review(self, rev, bid):
        """docstring for add_review"""
        new_rev = {
            "id" : len(self.reviews)+1,
            "businessId" : int(bid),
            "userId" : session["id"],
            "text" : rev["text"]
        }
        self.reviews.append(new_rev)
        return {"success":True, "msg":"Review created successfully", "reviews":self.reviews}

    def get_all_reviews(self):
        """docstring for getAllReviews"""
        return self.reviews

    def get_business_reviews(self, bid):
        """docstring for get_business_reviews"""
        output = []
        for review in self.reviews:
            if review["businessId"] == int(bid):
                output.append(review)
        # if len(output) > 0:
        return {"success":True, "reviews":output}
        # return {"success":False, "msg":"No reviews associated with businessId"+bid}
