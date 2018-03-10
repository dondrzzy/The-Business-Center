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
        return jsonify(result), 422

    # paginante businesses
    @staticmethod
    def get_businesses(page, limit, search_string, location, category):
        """docstring for paginating through the business"""
        filters = {}
        # generate filters
        if location is not None:
            filters["location"] = location
        if category is not None:
            filters["category"] = category
        res = Business.get_businesses(page, limit, search_string, filters)
        if res["success"]:
            return jsonify(res), 200
        return jsonify(res), 404


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
        return jsonify(result), 422

    # get single bsuiness
    @staticmethod
    def get_business(business_id):
        """docstring for get business"""
        res = Business.get_business(business_id)
        if res["success"]:
            return jsonify(res), 200
        return jsonify(res), 404

    # get single bsuiness
    @staticmethod
    def check_business(business_id):
        """docstring for get business"""
        return Business.get_business(business_id)

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
