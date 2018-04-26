""" docstring for busines model """
from sqlalchemy import ForeignKey
from app import db
from app.models.user import User
from app.models.category import Category

# from app.model import Business
class Business(db.Model):
    """docstring for Business model class """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('category.id'), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    user = db.relationship(User, backref=db.backref('business', cascade='all, delete'))
    category = db.relationship(Category, backref='business')

    def register_business(self):
        """ registers a business """
        if self.category_exists():
            db.session.add(self)
            db.session.commit()
            return {"success":True, "message":"Business Created"}
        return {"success": False, "message": "Incorrect business category"}
    
    def category_exists(self):
        category = Category.query.filter_by(id=self.category_id).first()
        if not category:
            return False
        return True


    @staticmethod
    def get_businesses(page, limit, search_string, location, filters):
        """ returns all businesses"""

        result = Business.query

        if search_string is not None:
            result = result.filter(Business.name.ilike("%"+search_string+"%"))
        if location is not None:
            result = result.filter(Business.location.ilike("%"+location+"%"))
        if bool(filters):
            result = result.filter_by(**filters)
        return {"paginate": result.paginate(page, limit, False), "total": result.count()}


    @staticmethod
    def get_business(business_id):
        """return a single business """
        return Business.query.filter_by(id=business_id).first()

    @staticmethod
    def update_business(business_id, business):
        """ updates a business """
        registered_business = Business.query.filter_by(id=business_id).first()
        registered_business.name = business["name"].title()
        registered_business.category_id = business["category"]
        registered_business.location = business["location"].title()
        db.session.commit()
        return registered_business

    @staticmethod
    def delete_business(business_id):
        """ deletes a business """
        # get business
        print(business_id)
        business = Business.query.filter_by(id=business_id).first()
        db.session.delete(business)
        db.session.commit()
