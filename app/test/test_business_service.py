""" docstring for testing business controller """
import unittest
from app.controllers.business_controller import BusinessController

class TestBusinessController(unittest.TestCase):
    """ docstring for testApp class """
    def setUp(self):
        """ init set up """
        self.business_controller = BusinessController()

    def test_missing_inputs(self):
        """ tests for missing acc credentials """
        b_obj = {
            "name":"Business",
            "category":"IT"
        }
        res = self.business_controller.register_business(9, b_obj)
        self.assertFalse(res["success"])

    def test_reg_error_resp(self):
        """ tests for the error response """
        b_obj = {
            "name":"Business",
            "category":"IT"
        }
        res = self.business_controller.register_business(9, b_obj)
        self.assertEqual(res["msg"], "Business location ('location') is required")

    def test_get_unknown_business(self):
        """ tests for getting uknown business """
        res = self.business_controller.get_business('sdjasdjbhasY')
        self.assertFalse(res["success"])

    def test_delete_inavlid_business(self):
        """ tests for deleting unknown business """
        res = self.business_controller.delete_business('sdjasdjbhasY', 9)
        self.assertFalse(res["success"])
