"""Business Class"""
from app.models.business import BusinessModel


BM = BusinessModel()

class BusinessController():
    """ Business Class """
    def __init__(self, arg=0):
        self.arg = arg

    def register_business(self, business):
        """register_business"""

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

        return BM.register_business(b_obj)

    # get all businesses
    def get_all_businesses(self):
        """get_all_businesses"""
        return BM.get_all_businesses()

    def update_business(self, bid, business):
        """update_business"""
        if bid.isdigit():

            b_obj = {}
            if "name" not in business and "category" not in business and "location" not in business:
                return {"success":False, "msg":"Nothing to update"}

            if "name" in business:
                b_obj["name"] = business["name"]
            if "category" in business:
                b_obj["category"] = business["category"]
            if "location" in business:
                b_obj["location"] = business["location"]


            return BM.update_business(bid, b_obj)

        return {"success":False, "msg":"Invalid business id"}

    # get single bsuiness
    def get_business(self, bid):
        """get_business"""
        if bid.isdigit():
            return BM.get_business(bid)
        return {"success":False, "msg":"Invalid business id"}

    # delete business
    def delete_business(self, bid):
        """delete_business"""
        if bid.isdigit():
            return BM.delete_business(bid)
        return {"success":False, "msg":"Invalid business id"}
