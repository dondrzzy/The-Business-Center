""" docstring for busines model """
from sqlalchemy import ForeignKey
from app import db
from app import jsonify
from app.models.user import User

# from app.model import Business
class Business(db.Model):
    """docstring for Business model class """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(80), nullable=False)
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

        paginate = result.paginate(page, limit, False)

        businesses = paginate.items
        output = []
        for business in businesses:
            business_object = {
                'id':business.id,
                'name':business.name,
                'category':business.category,
                'location':business.location,
                'user':business.user.name
            }
            output.append(business_object)
        next_page = paginate.next_num \
            if paginate.has_next else None
        prev_page = paginate.prev_num \
            if paginate.has_prev else None
        if len(output) > 0:
            return {"success":True, "businesses":output, "next_page":next_page, "prev_page":prev_page}
        return {"success":False, "businesses":output}

    @staticmethod
    def get_business(business_id):
        """return a single business """
        business = Business.query.filter_by(id=business_id).first()
        if not business:
            return {"success":False, "message":"Business with id "+business_id+" not found"}
        business_object = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return {"success":True, "business":business_object}

    @staticmethod
    def update_business(user_id, business_id, _business):
        """ updates a business """
        business = Business.query.filter_by(id=business_id).first()
        if not business:
            return jsonify({"success":False,
                            "message":"Business with id "+business_id+" not found"}), 404

        if business.user_id != user_id:
            return jsonify({"success":False, "message":"You can not perform that action"}), 401

        business.name = _business["name"]
        business.category = _business["category"]
        business.location = _business["location"]
        db.session.commit()
        business_object = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return jsonify({"success":True, "message":"Business updated successfully",
                        "business":business_object}), 200

    @staticmethod
    def delete_business(business_id, user_id):
        """ deletes a business """
        # get business
        business = Business.query.filter_by(id=business_id).first()
        if not business:
            return jsonify({"success":False,
                            "message":"Business with id "+business_id+" not found"}), 404
            # check owner
        if business.user_id != user_id:
            return jsonify({"success":False,
                            "message":"You can not perform that action"}), 401

        db.session.delete(business)
        db.session.commit()

        return jsonify({"success":True, "message":"Business successfully deleted"}), 200
