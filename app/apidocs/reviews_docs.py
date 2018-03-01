class Reviewdocs(object):
    """docstring for Reviewdocs"""
    def __init__(self, arg=0):
        self.arg = arg

    def post_get_reviews():
        return {
            "get" : {
              "tags" : [ "review" ],
              "summary" : "Get business reviews",
              "description" : "This can only be done by any user.",
              "operationId" : "getBusinessReviews",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "name" : "businessId",
                "in" : "path",
                "description" : "ID of business that whose reviews are to be fetched",
                "required" : True,
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_3"
                  }
                }
              }
            },
            "post" : {
              "tags" : [ "review" ],
              "summary" : "Post business review",
              "description" : "This can only be done by an authenticated user.",
              "operationId" : "postReview",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "name" : "businessId",
                "in" : "path",
                "description" : "ID of business being reviewed",
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
                  "$ref" : "#/definitions/Review"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_4"
                  }
                }
              }
            }
          }
        