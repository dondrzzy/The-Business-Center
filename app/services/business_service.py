"""docstring for Business Controller"""
from app.models.business import BusinessModel
BM = BusinessModel()
class BusinessService(object):
    """docstring for Business Class"""
    def __init__(self, arg=0):
        self.arg = arg

    def register_business(self, uid, business):
        """docstring for register business"""
        fields = ["name", "category", "location"]
        res = self.check_req_fields(business, fields)
        if res["success"]:
            b_obj = {
                "name" : business["name"],
                "category" : business["category"],
                "location" : business["location"]
            }

            BM.register_business(uid, b_obj)
            return {"success":True, "msg":"Business Created"}
        return res

    # get all businesses
    def get_all_businesses(self):
        """docstring for get all business"""
        return BM.get_all_businesses()

    def update_business(self, uid, bid, business):
        """docstring for updating a business"""
        fields = ["name", "category", "location"]
        res = self.check_req_fields(business, fields)
        if res["success"]:
            b_obj = {
                "name" : business["name"],
                "category" : business["category"],
                "location" : business["location"]
            }
            return BM.update_business(uid, bid, b_obj)
        return res

    # get single bsuiness
    def get_business(self, bid):
        """docstring for get business"""
        if bid.isdigit():
            return BM.get_business(bid)
        return {"success":False, "msg":"Invalid business id"}

    # delete business
    def delete_business(self, bid, uid):
        """docstring for delete business"""
        if bid.isdigit():
            return BM.delete_business(bid, uid)
        return {"success":False, "msg":"Invalid business id"}

    def check_req_fields(self, obj, fields):
        """checks required fields"""
        for field in fields:
            if field not in obj:
                return {"success":False, "msg":"Business "+field +" ('"+field+ "') is required"}
        return {"success":True}
