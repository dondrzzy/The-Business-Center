""" docstring for review controller """
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.services.user_service import UserService


class Review(db.Model):
    """ docstring for review class/model """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    business_id = db.Column(db.Integer, ForeignKey('business.id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)


    def add_review(self):
        """ docstring for add review fn"""
        db.session.add(self)
        db.session.commit()

    def get_business_reviews(business_id):
        """ return all reviews attached to this business """
        reviews = Review.query.filter_by(business_id=business_id).all()
        if not reviews:
            return {"success":False, "msg":"No Business Reviews"}
        output = []
        for review in reviews:
            review_object = {
                'id':review.id,
                'text':review.text,
                'user':US.get_user(review.user_id)["user"]
            }
            output.append(review_object)
        return {"success":True, "reviews":output}
