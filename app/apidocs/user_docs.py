class Userdocs(object):
    """docstring for Userdocs"""
    def __init__(self, arg=0):
        self.arg = arg
        
    def register_user():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Create user",
              "description" : "This can only be done by anyone.",
              "operationId" : "createUser",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "in" : "body",
                "name" : "body",
                "description" : "Created user object",
                "required" : True,
                "schema" : {
                  "$ref" : "#/definitions/User"
                }
              } ],
              "responses" : {
                "default" : {
                  "description" : "Account created successfully"
                }
              }
            }
          }

    def login_user():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Logs user into the application",
              "description" : "This can only be done by registered users.",
              "operationId" : "loginUser",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "in" : "body",
                "name" : "body",
                "description" : "The user object",
                "required" : True,
                "schema" : {
                  "$ref" : "#/definitions/body"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "successful operation",
                  "schema" : {
                    "type" : "string"
                  }
                },
                "400" : {
                  "description" : "email is required/password is required"
                }
              }
            }
          }
    def reset_password():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Resets the user's password",
              "operationId" : "resetUserPassword",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "in" : "body",
                "name" : "body",
                "description" : "The user object containing new password",
                "required" : True,
                "schema" : {
                  "$ref" : "#/definitions/body_1"
                }
              } ],
              "responses" : {
                "200" : {
                  "description" : "Password reset successfully",
                  "schema" : {
                    "type" : "string"
                  }
                },
                "400" : {
                  "description" : "email is required/password is required/passwords do not match"
                }
              }
            }
          }
    def logout():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Logs out current logged in user",
              "operationId" : "logoutUser",
              "produces" : [ "application/json" ],
              "parameters" : [ ],
              "responses" : {
                "default" : {
                  "description" : "successful operation"
                }
              }
            }
          }