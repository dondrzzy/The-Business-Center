"""docstring for Business Controller"""
import re
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
            valid_input_res = self.validate_business_input(business)
            if valid_input_res["success"]:
                Business(user_id=user_id, name=business["name"], category=business["category"],
                         location=business["location"]).register_business()
                return jsonify({"success":True, "message":"Business Created"}), 201
            return jsonify(valid_input_res), 422
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
        paginate = Business.get_businesses(page, limit, search_string, filters)
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
            return jsonify({"success":True, "businesses":output,
                            "next_page":next_page, "prev_page":prev_page}), 200
        return jsonify({"success":False, "businesses":output}), 404

    # paginante user businesses
    @staticmethod
    def get_user_businesses(page, limit, search_string, location, category, user_id):
        """docstring for paginating through the business"""
        filters = {}
        # generate filters
        if location is not None:
            filters["location"] = location
        if category is not None:
            filters["category"] = category
        if user_id is not None:
            filters["user_id"] = user_id
        paginate = Business.get_businesses(page, limit, search_string, filters)
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
            return jsonify({"success":True, "businesses":output,
                            "next_page":next_page, "prev_page":prev_page}), 200
        return {"success":False, "businesses":output}, 404

    def update_business(self, user_id, business_id, business):
        """
        docstring for updating a business
        get the businessId of the business to update
        get userId of user requesting to update
        check if all required field have been passed
        validate the user input
        check for updating authority
        update the business

        """
        fields = ["name", "category", "location"]
        result = self.check_req_fields(business, fields)
        if result["success"]:
            valid_input_res = self.validate_business_input(business)
            if valid_input_res["success"]:

                _business = Business.get_business(business_id)

                if not _business:
                    return jsonify({"success":False,
                                    "message":"Business\
                                    with id "+business_id+" not found"}),404

                if _business.user_id != user_id:
                    return jsonify({"success":False,
                                    "message":"You can not perform that action"}), 401

                _business = Business.update_business(business_id, business)
                business_object = {
                    'id':_business.id,
                    'name':_business.name,
                    'category':_business.category,
                    'location':_business.location
                }
                return jsonify({"success":True, "message":"Business updated successfully",
                                "business":business_object}), 200
            return jsonify(valid_input_res), 422
        return jsonify(result), 422

    # check business exists
    @staticmethod
    def check_business(business_id):
        """docstring for get business"""
        return  Business.get_business(business_id)

    # get single business
    def get_business(self, business_id):
        """docstring for get business"""
        business = self.check_business(business_id)
        if not business:
            return jsonify({"success":False,
                            "message":"Business with id "+business_id+" not found"}), 404
        business_object = {
            'id':business.id,
            'name':business.name,
            'category':business.category,
            'location':business.location
        }
        return jsonify({"success":True, "business":business_object}), 200

    # delete business
    @staticmethod
    def delete_business(business_id, user_id):
        """docstring for delete business"""
        business = Business.get_business(business_id)
        if not business:
            return jsonify({"success":False,
                            "message":"Business with id "+business_id+" not found"}), 404

        if business.user_id != user_id:
            return jsonify({"success":False, "message":"You can not perform that action"}), 401
        Business.delete_business(business_id)
        return jsonify({"success":True, "message":"Business successfully deleted"}), 200

    @staticmethod
    def check_req_fields(_object, fields):
        """checks required fields"""
        for field in fields:
            if field not in _object:
                return {"success":False, "message":"Business "+field +" is required"}
        return {"success":True}

    @staticmethod
    def validate_business_input(input_data):
        """ vaidate business input for empty and invalid fields """
        if 'name' in input_data:
            if not bool(re.fullmatch('[A-Za-z]{2,50}( [A-Za-z]{2,50})?', input_data["name"])):
                return {"success":False, "message":"Invalid business name"}
        # validate email
        if 'category' in input_data:
            if not bool(re.fullmatch('[A-Za-z]{2,50}( [A-Za-z]{2,50})?', input_data["category"])):
                return {"success":False, "message":"Invalid business category"}

        # validate password
        if 'location' in input_data:
            if not bool(re.fullmatch('[A-Za-z]{2,50}( [A-Za-z]{2,50})?', input_data["location"])):
                return {"success":False, "message":"Invalid business location"}

        return {"success":True}
