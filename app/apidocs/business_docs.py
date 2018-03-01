class Businessdocs(object):
    """docstring for Businessdocs"""
    def __init__(self, arg=0):
        self.arg = arg

    def post_get_businesses():
        return {
            "get" : {
              "tags" : [ "business" ],
              "summary" : "Get all business",
              "description" : "This can only be done by any user.",
              "operationId" : "getAllBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200"
                  }
                }
              }
            },
            "post" : {
              "tags" : [ "business" ],
              "summary" : "Create business",
              "description" : "This can only be done by a logged in user.",
              "operationId" : "createBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "in" : "body",
                "name" : "body",
                "description" : "Created Business object",
                "required" : True,
                "schema" : {
                  "$ref" : "#/definitions/Business"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_1"
                  }
                }
              }
            }
          }

    def get_put_delete_business():
        return {
            "get" : {
              "tags" : [ "business" ],
              "summary" : "Get a business",
              "description" : "This can only be done by any user.",
              "operationId" : "getBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "name" : "businessId",
                "in" : "path",
                "description" : "ID of business that needs to be updated",
                "required" : True,
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200"
                  }
                }
              }
            },
            "put" : {
              "tags" : [ "business" ],
              "summary" : "Update business",
              "description" : "This can only be done by an authenticated user.",
              "operationId" : "updateBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "name" : "businessId",
                "in" : "path",
                "description" : "ID of business that needs to be updated",
                "required" : True,
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
              }, {
                "in" : "body",
                "name" : "body",
                "description" : "Updated business object",
                "required" : True,
                "schema" : {
                  "$ref" : "#/definitions/Business"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_2"
                  }
                }
              }
            },
            "delete" : {
              "tags" : [ "business" ],
              "summary" : "Deletes a business",
              "operationId" : "deleteBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "name" : "businessId",
                "in" : "path",
                "description" : "Business id to delete",
                "required" : True,
                "type" : "integer",
                "format" : "int64"
              } ],
              "responses" : {
                "200" : {
                  "description" : "Business deleted successfully"
                },
                "404" : {
                  "description" : "Business not found"
                }
              }
            }
          }

        
