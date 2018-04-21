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
                    "$ref" : "#/definitions/inline_response_200_6"
                  }
                },
                "404" : {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_404_1"
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
              },
              {
                "in" : "header",
                "name" : "x-access-token",
                "description" : "Authorization token",
                "required" : True
              } ],
              "responses" : {
                "201" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_201_1"
                  }
                },
                "401" : {
                  "description" : "operation successful,",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_401_1"
                  }
                },
                "404" : {
                  "description" : "operation unsuccessful, incorrect business id",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_404_2"
                  }
                }
              }
            }
          }
        