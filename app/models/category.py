""" docstring for busines model """
from app import db
from app.models.user import User
import enum

class Category(db.Model):
    """docstring for Business model class """
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Enum("Approved", "Pending", name="status"), nullable=False, default="Approved")

    def register_category(self):
        """ registers a category """
        if self.check_category():
            return {"success": False, "message": "Category already exists"}
        db.session.add(self)
        db.session.commit()
        return {"success":True, "message":"Category Created"}
    @staticmethod
    def get_categories():
        """ get all categories """
        return Category.query.all()
    @staticmethod
    def delete_category(category_id):
        """ deletes a category """
        # get business
        category = Category.query.filter_by(id=category_id).first()
        db.session.delete(category)
        db.session.commit()
    def check_category(self):
        category = Category.query.filter_by(category = self.category).first()
        if not category:
            print('not exists')
            return False
        print('exists')
        return True
