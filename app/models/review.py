""" docstring for review controller """
from sqlalchemy import ForeignKey
from app import db
from app.models.user import User
from app.models.business import Business



class Review(db.Model):
    """ docstring for review class/model """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    business_id = db.Column(db.Integer, ForeignKey('business.id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = db.relationship(User, backref='review')
    business = db.relationship(Business, backref='review')


    def add_review(self):
        """ docstring for add review fn"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
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
                'user':review.user.name
            }
            output.append(review_object)
        return {"success":True, "reviews":output}
