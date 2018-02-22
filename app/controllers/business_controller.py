from app.models.business import BusinessModel
BusinessModel = BusinessModel()
class BusinessController(object):
    def __init__(self, arg=0):
        self.arg = arg

    def register_business(self, uid, business):
        if "name" not in business:
            return {"success":False, "msg":"Business name ('name') is required"}
        elif "category" not in business:
            return {"success":False, "msg":"Category is required"}
        elif "location" not in business:
            return {"success":False, "msg":"Location is required"}

        b_obj = {
            "name" : business["name"],
            "category" : business["category"],
            "location" : business["location"]            
        }

        BusinessModel.register_business(uid, b_obj)
        return {"success":True, "msg":"Business Created"}

    # get all businesses
    def get_all_businesses(self):
        return BusinessModel.get_all_businesses()
    
    def update_business(self, uid, bid, business):
        if "name" not in business:
            return {"success":False, "msg":"Business name ('name') is required"}
        elif "category" not in business:
            return {"success":False, "msg":"Category is required"}
        elif "location" not in business:
            return {"success":False, "msg":"Location is required"}

        b_obj = {
            "name" : business["name"],
            "category" : business["category"],
            "location" : business["location"]            
        }

        return BusinessModel.update_business(uid, bid, b_obj)

    # get single bsuiness
    def get_business(self, bid):
        if bid.isdigit():
            return BusinessModel.get_business(bid)
        return {"success":False, "msg":"Invalid business id"}

    # delete business
    def delete_business(self, bid, uid):
        if bid.isdigit():
            return BusinessModel.delete_business(bid, uid)
        return {"success":False, "msg":"Invalid business id"}

