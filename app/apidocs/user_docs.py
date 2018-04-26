class Userdocs(object):
    """docstring for Userdocs"""
    def __init__(self, arg=0):
        self.arg = arg
    @staticmethod
    def register_user():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Create user",
              "description" : "Any unregistered user can register. Required attributes include name, email and password. The password should be strong, i.e. with an upper case character, special character and/or a number and should be more than 6 characters",
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
                "201" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_201"
                  }
                },
                "409" : {
                  "description" : "operation unsuccessful, email exists",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_409"
                  }
                },
                "422" : {
                  "description" : "operation unsuccessful, invalid user input",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_422"
                  }
                }
              }
            }
          }
    @staticmethod
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
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200"
                  }
                },
                "401" : {
                  "description" : "operation unsuccessful, Wrong password",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_401"
                  }
                },
                "404" : {
                  "description" : "operation unsuccessful, user not found",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_404"
                  }
                }
              }
            }
          }
    @staticmethod
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
                  "description" : "operation successful, password reset successfully",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_1"
                  }
                },
                "404" : {
                  "description" : "operation unsuccessful, user not found",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_404"
                  }
                },
                "422" : {
                  "description" : "operation unsuccessful, Invalid user input",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_422"
                  }
                }
              }
            }
          }
    @staticmethod
    def logout():
        return {
            "post" : {
              "tags" : [ "user" ],
              "summary" : "Logs out current logged in user",
              "operationId" : "logoutUser",
              "produces" : [ "application/json" ],
              "parameters" : [{
                "in" : "header",
                "name" : "x-access-token",
                "description" : "Authorization token",
                "required" : True
              } ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_200_2"
                  }
                },
                "401" : {
                  "description" : "operation successful, invalid token",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_401_1"
                  }
                }
              }
            }
          }