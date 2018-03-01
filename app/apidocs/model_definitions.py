class Define(object):
    """docstring for User"""
    def __init__(self, arg=0):
        self.arg = arg

    def user():
        return {
            "type" : "object",
            "properties" : {
              "id" : {
                "type" : "integer",
                "format" : "int64"
              },
              "name" : {
                "type" : "string"
              },
              "email" : {
                "type" : "string"
              },
              "password" : {
                "type" : "string"
              },
              "confirm password" : {
                "type" : "string"
              }
            },
            "example" : {
              "password" : "password",
              "confirm password" : "confirm password",
              "name" : "name",
              "id" : 0,
              "email" : "email"
            },
            "xml" : {
              "name" : "User"
            }
          }

    def business():
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
              "id" : 0,
              "category" : "category",
              "userId" : 6
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
              "businessId" : 1,
              "id" : 0,
              "text" : "text",
              "userId" : 6
            },
            "xml" : {
              "name" : "Review"
            }
          }

    def api_resopnse():
        return 

        
        