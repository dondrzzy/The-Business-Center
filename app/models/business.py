""" docstring for busines model """
from app import db
from app.model import Business
class BusinessModel(object):
    """docstring for Business model class """
    def __init__(self, businesses=[]):
        self.businesses = businesses

    def register_business(self, uid, bus):
        """ registers a business """
        business = Business(uid, bus["name"], bus["category"], bus["location"])
        db.session.add(business)
        db.session.commit()

    def get_all_businesses(self):
        """ returns all businesses"""
        businesses = Business.query.all()
        output = []
        for business in businesses:
            b_obj = {
                'id':business.id,
                'name':business.name,
                'category':business.category,
                'location':business.location
            }
            output.append(b_obj)
        return {"businesses":output}

    def get_business(self, bid):
        """return a single business """
        business = Business.query.filter_by(id=bid).first()
        if not business:
            return {"success":False, "msg":"Business with id "+bid+" not found"}
        b_obj = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return {"success":True, "business":b_obj}


    def update_business(self, uid, bid, bus):
        """ updates a business """
        business = Business.query.filter_by(id=bid).first()
        if not business:
            return {"success":False, "msg":"Business with id "+bid+" not found"}

        if business.uid != uid:
            return {"success":False, "msg":"You can not perform that action"}

        business.name = bus["name"]
        business.category = bus["category"]
        business.location = bus["location"]
        db.session.commit()
        b_obj = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return {"success":True, "msg":"Business updated successfully", "business":b_obj}

    def delete_business(self, bid, uid):
        """ deletes a business """
        # get business
        business = Business.query.filter_by(id=bid).first()
        if not business:
            return {"success":False, "msg":"Business with id "+bid+" not found"}
            # check owner
        if business.uid != uid:
            return {"success":False, "msg":"You can not perform that action"}

        db.session.delete(business)
        db.session.commit()

        return {"success":True, "msg":"Business successfully deleted"}
