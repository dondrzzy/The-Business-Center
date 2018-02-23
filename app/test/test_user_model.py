"""docstring for UserModel"""
import unittest
from app.models.user import UserModel


class TestUserController(unittest.TestCase):
    """docstring for TestUser"""
    def setUp(self):
        """docstring for setUp"""
        self.user_model = UserModel()

    def test_register_use(self):
        """docstring for testing user registration"""
        test_user = {"name":"Sibo", "email":"test@gmail.com", "password":"1234"}
        res = self.user_model.register_user(test_user)["success"]
        self.assertFalse(res, msg="Invalid model register user function")

    # test if it denies identical emails
    def test_get_user(self):
        """docstring for get users fn"""
        self.assertEqual(len(self.user_model.get_users()), 2, msg="Invalid model get user function")

    def test_no_users(self):
        """docstring for testing get no o users fn"""
        self.assertEqual(len(self.user_model.get_users()), 2, msg="Invalid model get user function")
