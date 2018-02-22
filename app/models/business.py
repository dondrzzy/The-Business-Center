from app import db
from app.schemas import Business
class BusinessModel(object):
    def __init__(self, businesses = []):
        self.businesses = businesses

    def register_business(self, uid, b):     
        business = Business(uid, b["name"], b["category"], b["location"])
        db.session.add(business)
        db.session.commit()
    
    def get_all_businesses(self):
        businesses = Business.query.all()   
        output = []
        for b in businesses:
            b_obj = {
                'id':b.id,
                'name':b.name,
                'category':b.category,
                'location':b.location
            }
            output.append(b_obj) 
        return {"businesses":output}

    def get_business(self, bid):
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


    def update_business(self, uid, bid, b):

        business = Business.query.filter_by(id=bid).first()
        if not business:
            return {"success":False, "msg":"Business with id "+bid+" not found"}

        if business.uid != uid:
            return {"success":False, "msg":"You can not perform that action"}

        business.name = b["name"]
        business.category = b["category"]
        business.location = b["location"]
        db.session.commit()
        b_obj = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return {"success":True, "msg":"Business updated successfully", "business":b_obj}

    def delete_business(self, bid, uid):
        # get business
        business = Business.query.filter_by(id=bid).first()
        if not business:
            return {"success":False, "msg":"Business with id "+bid+" not found"}
            # check owner
        if business.uid != uid:
            return {"success":False, "msg":"You can not perform that action"}

        db.session.delete(business)
        db.session.commit()

        return {"succcess":True, "msg":"Business successfully deleted"}

        
