class Businessdocs(object):
    """docstring for Businessdocs"""
    def __init__(self, arg=0):
        self.arg = arg

    def post_get_businesses():
        return {
            "get" : {
              "tags" : [ "business" ],
              "summary" : "Get all business",
              "description" : "Returns a list of all businesses. Paginated results by default",
              "operationId" : "getAllBusiness",
              "produces" : [ "application/json" ],
              "parameters" : [ {
                "in" : "query",
                "name" : "q",
                "description" : "business search parameter",
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
                },
                {
                "in" : "query",
                "name" : "page",
                "description" : "pagination page",
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
                },
                {
                "in" : "query",
                "name" : "limit",
                "description" : "limit per page",
                "type" : "integer",
                "minimum" : 1,
                "format" : "int64"
                },
                {
                "in" : "query",
                "name" : "category",
                "description" : "filter by category",
                "type" : "string"
                },
                {
                "in" : "query",
                "name" : "location",
                "description" : "filter by location",
                "type" : "string"
                }
              ],
              "responses" : {
                "200" : {
                  "description" : "operation successful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : True
                      },
                      "prev_page" : {
                        "type" : "integer",
                        "example" : "null"
                      },
                      "next_page" : {
                        "type" : "integer",
                        "example" : 2
                      },
                      "businesss" : {
                        "type" : "array",
                        "items" : {
                          "$ref" : "#/definitions/inline_response_200_3_businesss"
                        }
                      }
                    },
                    "example" : {
                      "next_page" : 2,
                      "businesss" : [ {
                        "name" : "name",
                        "location" : "location",
                        "id" : 1,
                        "category" : "category",
                        "userId" : 1
                      }],
                      "success" : True,
                      "prev_page" : "null"
                    }
                  }
                },
                "404": {
                  "description" : "operation unsuccessful, businesses not found",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "businesses" : {
                        "type":"array",
                        "example":[]
                      }
                    }
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
              }, {
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
                  "description" : "operation unsuccessful, unauthorized",
                  "schema" : {
                    "$ref" : "#/definitions/inline_response_401_1"
                  }
                },
                "422" : {
                  "description" : "operation unsuccessful, invalid business data",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Invalid business category"
                      }
                    }
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
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : True
                      },
                      "business" : {
                        "type" : "object",
                        "example" : {
                          "name" : "name",
                          "location" : "location",
                          "id" : 1,
                          "category" : "category",
                          "userId" : 1
                        }
                      }
                    }
                  }
                },
                "404": {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Business with id 2 not found"
                      }
                    }
                  }
                },

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
              },
              {
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
                "401": {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "You can not perform that action"
                      }
                    }
                  }
                },
                "404": {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Business with id 4 not found"
                      }
                    }
                  }
                },
                "422": {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Invalid business category"
                      }
                    }
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
              },
              {
                "in" : "header",
                "name" : "x-access-token",
                "description" : "Authorization token",
                "required" : True
              } ],
              "responses" : {
                "200" : {
                  "description" : "Business deleted successfully",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : True
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Business successfully deleted"
                      }
                    }
                  }
                },
                "404" : {
                  "description" : "Business not found",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "Business with id 2 not found"
                      }
                    }
                  }
                },
                "401": {
                  "description" : "operation unsuccessful",
                  "schema" : {
                    "properties" : {
                      "success" : {
                        "type" : "boolean",
                        "example" : False
                      },
                      "message" : {
                        "type" : "string",
                        "example" : "You can not perform that action"
                      }
                    }
                  }
                }
              }
            }
          }

        
