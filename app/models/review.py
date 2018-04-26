""" docstring for review controller """
from datetime import datetime
from sqlalchemy import ForeignKey
from app import db
from app.models.user import User
from app.models.business import Business



class Review(db.Model):
    """ docstring for review class/model """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    business_id = db.Column(db.Integer, ForeignKey('business.id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    user = db.relationship(User, backref='review')
    business = db.relationship(Business, backref=db.backref('review', cascade='all, delete'))


    def add_review(self):
        """ docstring for add review fn"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_business_reviews(business_id):
        """ return all reviews attached to this business """
        return  Review.query.filter_by(business_id=business_id).all()
