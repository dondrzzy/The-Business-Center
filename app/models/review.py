""" docstring for review controller """
from app import db
from app.schemas import Review
from app.controllers.user_controller import UserController

UC = UserController()

class ReviewModel(object):
    """ docstring for review class/model """
    def __init__(self, reviews=[]):
        self.reviews = reviews


    def add_review(self, rev, bid, uid):
        """ docstring for add review fn"""
        db.session.add(Review(rev["text"], bid, uid))
        db.session.commit()

    def get_business_reviews(self, bid):
        """ docstrfor get business reviews """
        reviews = Review.query.filter_by(bid=bid).all()
        if not reviews:
            return {"success":False, "msg":"No Business Reviews"}
        output = []
        for rev in reviews:
            r_obj = {
                'id':rev.id,
                'text':rev.text,
                'user':UC.get_user(rev.uid)["user"]
            }
            output.append(r_obj)
        return {"success":True, "reviews":output}
