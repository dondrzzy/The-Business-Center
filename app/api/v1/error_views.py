""" Custom Error methods for the application """
from flask import jsonify
from app import app

@app.errorhandler(404)
def endpoint_not_found(error):
    """ Return 404 not found for unkown endpoints """
    return jsonify({"success":False, "error":str(error)}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """ Return 404 not found for unkown endpoints """
    return jsonify({"success":False, "error":str(error)}), 405

@app.errorhandler(500)
def internal_server_error(error):
    """ Return 500 not found for internal server error """
    return jsonify({"success":False, "error":str(error)}), 500
