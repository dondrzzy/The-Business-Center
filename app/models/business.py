""" docstring for busines model """
from sqlalchemy import ForeignKey
from app import db
from app.models.user import User

# from app.model import Business
class Business(db.Model):
    """docstring for Business model class """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    user = db.relationship(User, backref='business')

    def register_business(self):
        """ registers a business """
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def get_businesses(page, limit, search_string, filters):
        """ returns all businesses"""

        result = Business.query

        if search_string is not None:
            result = result.filter(Business.name.like("%"+search_string+"%"))

        if bool(filters):
            result = result.filter_by(**filters)

        return result.paginate(page, limit, False)


    @staticmethod
    def get_business(business_id):
        """return a single business """
        return Business.query.filter_by(id=business_id).first()

    @staticmethod
    def update_business(business_id, business):
        """ updates a business """
        registered_business = Business.query.filter_by(id=business_id).first()

        registered_business.name = business["name"]
        registered_business.category = business["category"]
        registered_business.location = business["location"]
        db.session.commit()
        return registered_business

    @staticmethod
    def delete_business(business_id):
        """ deletes a business """
        # get business
        business = Business.query.filter_by(id=business_id).first()

        db.session.delete(business)
        db.session.commit()
