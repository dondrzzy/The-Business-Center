"""docstring for BusinessModel"""
import unittest
from app.models.business import BusinessModel


class TestUserController(unittest.TestCase):
    """docstring for TestUser"""
    def setUp(self):
        """docstring for setUp"""
        self.business_model = BusinessModel()


    # test if it denies identical emails
    def test_get_all_user(self):
        """docstring for test_get_all_user"""
        length = len(self.business_model.get_all_businesses()["businesses"])
        self.assertEqual(length, 0, msg="Invalid model get businesses function")

    def test_get_invalid_business(self):
        """docstring for test_get_invalid_business"""
        res = self.business_model.get_business('3')["success"]
        self.assertFalse(res, msg="Invalid model get businesses function")
