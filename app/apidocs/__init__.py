from app.apidocs.user_docs import Userdocs
from app.apidocs.business_docs import Businessdocs
from app.apidocs.reviews_docs import Reviewdocs
from app.apidocs.model_definitions import Define
class Apidocs(object):
    """docstring for Apidocs"""
    def __init__(self, arg=0):
        super(Apidocs, self).__init__()
        self.arg = arg

    swagger_conf = {
        "swagger" : "2.0",
        "info" : {
          "description" : "The Business Center API is a RESTFUL API used to create, read, update businesses and post reviews to businesses. Users are supposed to sign up to create accounts inorder to add businesses and post reviews. Only authenticated users can update and delete businesses.\n",
          "version" : "1.0.0",
          "title" : "The Business Center Api"
        },
        "host" : "the-business-center-api.herokuapp.com",
        "basePath" : "",
        "tags" : [ {
          "name" : "user",
          "description" : "Operations about user"
        }, {
          "name" : "business",
          "description" : "Operations about business"
        }, {
          "name" : "review",
          "description" : "Operations about business reveiws"
        } ],
        "schemes" : [ "https" ],
        "paths" : {
          "/api/v1/auth/register" : Userdocs.register_user(),
          "/api/v1/auth/login" : Userdocs.login_user(),
          "/api/v1/auth/reset-password" : Userdocs.reset_password(),
          "/api/v1/auth/logout" : Userdocs.logout(),
          "/api/v1/businesses" : Businessdocs.post_get_businesses(),
          "/api/v1/businesses/{businessId}" : Businessdocs.get_put_delete_business(),
          "/api/v1/businesses/{businessId}/reviews" : Reviewdocs.post_get_reviews()
        },
        "definitions" : {
          "User" : Define.user(),
          "Business" : Define.business(),
          "Review" : Define.review(),
          "ApiResponse" : {
            "type" : "object",
            "properties" : {
              "code" : {
                "type" : "integer",
                "format" : "int32"
              },
              "success" : {
                "type" : "boolean"
              },
              "message" : {
                "type" : "string"
              }
            }
          },
          "body" : {
            "type" : "object",
            "properties" : {
              "email" : {
                "type" : "string"
              },
              "password" : {
                "type" : "string"
              }
            }
          },
          "body_1" : {
            "type" : "object",
            "properties" : {
              "email" : {
                "type" : "string"
              },
              "password" : {
                "type" : "string"
              },
              "confirm_password" : {
                "type" : "string"
              }
            }
          },
          "inline_response_200_businesss" : {
            "properties" : {
              "id" : {
                "type" : "integer",
                "example" : 1
              },
              "userId" : {
                "type" : "integer",
                "example" : 1
              },
              "name" : {
                "type" : "string"
              },
              "category" : {
                "type" : "string"
              },
              "location" : {
                "type" : "string"
              }
            },
            "example" : {
              "name" : "name",
              "location" : "location",
              "id" : 1,
              "category" : "category",
              "userId" : 1
            }
          },
          "inline_response_200" : {
            "properties" : {
              "success" : {
                "type" : "boolean",
                "example" : True
              },
              "businesss" : {
                "type" : "array",
                "items" : {
                  "$ref" : "#/definitions/inline_response_200_businesss"
                }
              }
            },
            "example" : {
              "businesss" : [ {
                "name" : "name",
                "location" : "location",
                "id" : 1,
                "category" : "category",
                "userId" : 1
              }, {
                "name" : "name",
                "location" : "location",
                "id" : 1,
                "category" : "category",
                "userId" : 1
              } ],
              "success" : True
            }
          },
          "inline_response_200_1" : {
            "properties" : {
              "success" : {
                "type" : "boolean",
                "example" : True
              },
              "msg" : {
                "type" : "string",
                "example" : "Business created successfully"
              }
            },
            "example" : {
              "msg" : "Business created successfully",
              "success" : True
            }
          },
          "inline_response_200_2" : {
            "properties" : {
              "success" : {
                "type" : "boolean",
                "example" : True
              },
              "msg" : {
                "type" : "string",
                "example" : "Business updated successfully"
              },
              "business" : {
                "$ref" : "#/definitions/Business"
              }
            },
            "example" : {
              "msg" : "Business updated successfully",
              "business" : {
                "name" : "name",
                "location" : "location",
                "id" : 0,
                "category" : "category",
                "userId" : 6
              },
              "success" : True
            }
          },
          "inline_response_200_3_reviews" : {
            "properties" : {
              "id" : {
                "type" : "integer",
                "example" : 1
              },
              "userId" : {
                "type" : "integer",
                "example" : 1
              },
              "businessId" : {
                "type" : "integer",
                "example" : 1
              },
              "text" : {
                "type" : "string"
              }
            },
            "example" : {
              "businessId" : 1,
              "id" : 1,
              "text" : "text",
              "userId" : 1
            }
          },
          "inline_response_200_3" : {
            "properties" : {
              "success" : {
                "type" : "boolean",
                "example" : True
              },
              "reviews" : {
                "type" : "array",
                "items" : {
                  "$ref" : "#/definitions/inline_response_200_3_reviews"
                }
              }
            },
            "example" : {
              "reviews" : [ {
                "businessId" : 1,
                "id" : 1,
                "text" : "text",
                "userId" : 1
              }, {
                "businessId" : 1,
                "id" : 1,
                "text" : "text",
                "userId" : 1
              } ],
              "success" : True
            }
          },
          "inline_response_200_4" : {
            "properties" : {
              "success" : {
                "type" : "boolean",
                "example" : True
              },
              "msg" : {
                "type" : "string",
                "example" : "Review posted successfully"
              }
            },
            "example" : {
              "msg" : "Review posted successfully",
              "success" : True
            }
          }
        },
        "externalDocs" : {
          "description" : "Find out more about the business center",
          "url" : "http://the-business-center.herokuapp.com"
        }
      }
        