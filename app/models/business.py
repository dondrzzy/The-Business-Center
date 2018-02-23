"""docstring for Review Model"""
from flask import session

class BusinessModel(object):
    """docstring for BusinessModel"""
    def __init__(self, businesses=[]):
        self.businesses = businesses

    def register_business(self, business):
        """docstring for register_business"""
        new_business = {
            "id" : len(self.businesses) + 1,
            "name" : business["name"],
            "category" : business["category"],
            "location" : business["location"],
            "user_id" : session["id"]
        }
        self.businesses.append(new_business)
        return {"success":True, "msg":business["name"]+" business registered successfully"}

    def get_all_businesses(self):
        """docstring for get_all_businesses"""
        return {"success":True, "businesses":self.businesses}

    def get_business(self, bid):
        """docstring for get_business"""
        for business in self.businesses:
            if business["id"] == int(bid):
                return {'Success':True, "business":business}
        return {'success':False, "msg":"Business with id "+bid+" not found"}

    def update_business(self, bid, _b):
        """docstring for update_business"""
        for business in self.businesses:
            # if business is found
            if business["id"] == int(bid):
                # confirm owner
                if business["user_id"] == session["id"]:
                    if "name" in _b:
                        business["name"] = _b["name"]
                    if "category" in _b:
                        business["category"] = _b["category"]
                    if "location" in _b:
                        business["location"] = _b["location"]
                    return {"success":True, "msg":"Business updated", "business":business}

                return {"success":False, "msg":"You cant perform that action"}

        return {"success":False, "msg":"Business with id "+bid+" not found"}

    def delete_business(self, bid):
        """docstring for delete_business"""
        for business in self.businesses:

            # get business using id
            if business["id"] == int(bid):

                # confirm ownership
                if business["user_id"] == session["id"]:
                    self.businesses.remove(business)
                    return {"success":True, "msg":"Business deleted successfully"}

                return {"success":False, "msg":"You can not perform that action"}

        return {"success":False, "msg":"Business with id "+bid+" not found"}
