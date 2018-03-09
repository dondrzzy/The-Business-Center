"""docstring for Business Controller"""
from flask import jsonify
from app.models.business import Business


class BusinessService(object):
    """docstring for Business Class"""
    def __init__(self, arg=0):
        self.arg = arg


    def register_business(self, user_id, business):
        """docstring for register business"""
        fields = ["name", "category", "location"]
        result = self.check_req_fields(business, fields)
        if result["success"]:
            Business(user_id=user_id, name=business["name"], category=business["category"],
                     location=business["location"]).register_business()
            return jsonify({"success":True, "message":"Business Created"}), 201
        return jsonify(result), 400

    # paginante businesses
    @staticmethod
    def get_businesses(page, limit, search_string, location, category):
        """docstring for paginating through the business"""
        return Business.get_businesses(page, limit, search_string, location, category)


    def update_business(self, user_id, business_id, business):
        """docstring for updating a business"""
        fields = ["name", "category", "location"]
        result = self.check_req_fields(business, fields)
        if result["success"]:
            business_object = {
                "name" : business["name"],
                "category" : business["category"],
                "location" : business["location"]
            }
            return Business.update_business(user_id, business_id, business_object)
        return jsonify(result), 400

    # get single bsuiness
    @staticmethod
    def get_business(business_id):
        """docstring for get business"""
        # if business_id.isdigit():
        return Business.get_business(business_id)
        # return {"success":False, "message":"Invalid business id"}

    # delete business
    @staticmethod
    def delete_business(business_id, user_id):
        """docstring for delete business"""
        return Business.delete_business(business_id, user_id)

    @staticmethod
    def check_req_fields(_object, fields):
        """checks required fields"""
        for field in fields:
            if field not in _object:
                return {"success":False, "message":"Business "+field +" ('"+field+ "') is required"}
        return {"success":True}
