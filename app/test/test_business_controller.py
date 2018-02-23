"""docstring for TestController"""
import unittest
from app.controllers.business_controller import BusinessController


class TestBusinessController(unittest.TestCase):
    """docstring for TestBusinessController"""
    def setUp(self):
        """intitial setup"""
        self.business_controller = BusinessController()

    def test_missing_register_info(self):
        """test_business_register_missing_crendentials"""
        test_business = {"name":"Business", "category":"IT"}
        res = self.business_controller.register_business(test_business)["success"]
        self.assertFalse(res, msg="Invalid register function")

    def test_get_all_business(self):
        """test_get_all_business"""
        length = len(self.business_controller.get_all_businesses()["businesses"])
        self.assertEqual(length, 0, msg="Invalid register function")

    def test_get_invalid_business(self):
        """test_get_invalid_business"""
        res = self.business_controller.get_business('e')["msg"]
        self.assertEqual(res, "Invalid business id", msg="Invalid register function")
   