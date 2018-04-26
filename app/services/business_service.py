"""docstring for Business Controller"""
import re
from flask import jsonify
from app.models.business import Business
from app.models.category import Category
from app.models.user import User

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
            print(valid_input_res)
            if valid_input_res["success"]:
                result = Business(user_id=user_id, name=business["name"].title(),
                                  category_id=business["category"],
                                  location=business["location"].title()).register_business()
                if result["success"]:
                    return jsonify(result), 201
                return jsonify(result), 404
            return jsonify(valid_input_res), 422
        return jsonify(result), 422

    def register_category(self, category):
        """ logic to register a categogry """
        fields = ["category","status"]
        result = self.check_cat_fields(category, fields)
        if result["success"]:
            if not bool(re.match('^[A-Za-z, ]{2,50} *$', category["category"])):
                return jsonify({"success":False, "message":"Invalid business category"}), 422
            if category["status"] not in ["Approved", "Pending"]:
                return jsonify({"success":False, "message":"Invalid category status"}), 422
            result = Category(category=category["category"].title(),
                              status=category["status"]).register_category()
            if result["success"]:
                return jsonify(result), 201
        return jsonify(result), 422
    
    @staticmethod
    def get_categories_json():
        """ return all categories """
        categories = Category.get_categories()
        output = []
        for category in categories:
            output.append({
                "category": category.category,
                "status": category.status,
                "id": category.id
            })
        return output

    def get_categories(self):
        return jsonify({"success":True, "categories": self.get_categories_json()}), 200

    # paginante businesses
    def get_businesses(self, page, limit, search_string, location, category):
        """docstring for paginating through the business"""
        if category is not None:
            try:
                int(category)
            except ValueError:
                return jsonify({'success':False, 'message':'Invalid category, must be an integer.'}), 400
        filters = {}
        # generate filters
        # if location is not None:
        #     filters["location"] = location
        if category is not None:
            filters["category_id"] = category
        result = Business.get_businesses(page, limit, search_string, location, filters)
        paginate =result["paginate"]
        businesses = paginate.items
        output = []
        for business in businesses:
            business_object = {
                'id':business.id,
                'name':business.name,
                'category':{
                    'category': business.category.category,
                    'status': business.category.status,
                    'id': business.category.id
                },
                'location':business.location,
                'user':{ 
                    'name': business.user.name,
                    'id': business.user.id
                }
            }
            output.append(business_object)
        next_page = paginate.next_num \
            if paginate.has_next else None
        prev_page = paginate.prev_num \
            if paginate.has_prev else None

        return jsonify({"success":True, "businesses":output,
                        "categories": self.get_categories_json(),
                        "next_page":next_page, "prev_page":prev_page,
                        "total": result["total"]}), 200

    # paginante user businesses
    def get_user_businesses(self, page, limit, search_string, location, category, user_id):
        """docstring for paginating through the business"""
        user = User.get_user(user_id)
        user_object = {
            'name': user.name,
            'email': user.email
        }
        filters = {}
        # generate filters
        if category is not None:
            filters["category"] = category
        if user_id is not None:
            filters["user_id"] = user_id
        result = Business.get_businesses(page, limit, search_string, location, filters)
        paginate = result["paginate"]
        businesses = paginate.items
        output = []
        for business in businesses:
            business_object = {
                'id':business.id,
                'name':business.name,
                'category':{
                    'category': business.category.category,
                    'status': business.category.status,
                    'id': business.category.id
                },
                'location':business.location,
                'user':{ 
                    'name': business.user.name,
                    'id': business.user.id
                }
            }
            output.append(business_object)
        next_page = paginate.next_num \
            if paginate.has_next else None
        prev_page = paginate.prev_num \
            if paginate.has_prev else None
        
        return jsonify({"success":True, "user": user_object, "businesses":output,
                        "categories": self.get_categories_json(),
                        "next_page":next_page, "prev_page":prev_page,
                        "total": result["total"]}), 200

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

                registered_business = Business.get_business(business_id)

                if not registered_business:
                    return jsonify({"success":False,
                                    "message":"Business\
                                    with id "+business_id+" not found"}), 404

                if registered_business.user_id != user_id:
                    return jsonify({"success":False,
                                    "message":"You can not perform that action"}), 401

                registered_business = Business.update_business(business_id, business)
                business_object = {
                    'id':registered_business.id,
                    'name':registered_business.name,
                    'category':{
                        'category': registered_business.category.category,
                        'status': registered_business.category.status,
                        'id': registered_business.category.id
                    },
                    'location':registered_business.location,
                    'user':{ 
                        'name': registered_business.user.name,
                        'id': registered_business.user.id
                    }
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
            'category':{
                'category': business.category.category,
                'status': business.category.status,
                'id': business.category.id
            },
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
    def check_cat_fields(_object, fields):
        """checks required fields"""
        for field in fields:
            if field not in _object:
                return {"success":False, "message":field +" is required"}
        return {"success":True}

    @staticmethod
    def validate_business_input(input_data):
        """ vaidate business input for empty and invalid fields """
        if 'name' in input_data:
            if not bool(re.match('^[A-Za-z, ]{2,50} *$', input_data["name"])):
                return {"success":False, "message":"Invalid business name"}
        if 'category' in input_data:
            print(input_data["category"])
            try:
                int(input_data["category"])
            except ValueError:
                return {"success":False, "message":"Invalid business category"}

        # validate password
        if 'location' in input_data:
            if not bool(re.match('^[A-Za-z, ]{2,50} *$', input_data["location"])):
                return {"success":False, "message":"Invalid business location"}
        return {"success":True}
