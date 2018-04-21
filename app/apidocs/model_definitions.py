class Define(object):
    """docstring for User"""
    def __init__(self, arg=0):
        self.arg = arg

    def user():
        return {
            "type" : "object",
            "properties" : {
              "name" : {
                "type" : "string"
              },
              "email" : {
                "type" : "string"
              },
              "password" : {
                "type" : "string"
              }
            },
            "example" : {              
              "name" : "name",
              "email" : "name@gmail.com",
              "password" : "#name@2000",
              "confirm_password" : "#name@2000"
            },
            "xml" : {
              "name" : "User"
            }
          }

    def business():
        return {
            "type" : "object",
            "properties" : {
              "name" : {
                "type" : "string",
                "description" : "Business name"
              },
              "category" : {
                "type" : "string",
                "description" : "Business category"
              },
              "location" : {
                "type" : "string",
                "description" : "Business location"
              }
            },
            "example" : {
              "name" : "name",
              "location" : "location",
              "category" : "category"
            },
            "xml" : {
              "name" : "Business"
            }
          }

    def review():
        return {
            "type" : "object",
            "properties" : {
              "id" : {
                "type" : "integer",
                "format" : "int64"
              },
              "userId" : {
                "type" : "integer",
                "format" : "int64"
              },
              "businessId" : {
                "type" : "integer",
                "format" : "int64"
              },
              "text" : {
                "type" : "string",
                "description" : "Business review text"
              }
            },
            "example" : {
              "text" : "text"
            },
            "xml" : {
              "name" : "Review"
            }
          }

    def api_resopnse():
        return 

        
        