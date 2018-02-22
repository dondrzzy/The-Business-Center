import unittest
from models.user import User
from models.business import Business
class TestUser(unittest.TestCase):
    """docstring for TestUser"""
    def setUp(self):
        self.user = User()
        self.business = Business()

    def test_user_register_init(self):
        test_user = {"id":1, "name":"Sibo", "email":"test@gmail.com", "password":"1234"}
        self.assertEqual(self.user.id, 0, msg="Invalid function")

    def test_user_register_email_exists(self):
        test_user = {"id":1, "name":"Sibo", "email":"test@gmail.com", "password":"1234"}
        self.assertFalse(self.user.register(test_user), msg="Invalid function")

    def test_user_register_email_not_exists(self):
        test_user = {"id":1, "name":"Sibo", "email":"test1@gmail.com", "password":"1234"}
        self.assertTrue(self.user.register(test_user), msg="Invalid function")

    def test_user_login_user_unkown(self):
        test_user = {"email":"test1@gmail.com"}
        self.assertFalse(self.user.login(test_user)["success"], msg="Invalid function")

    def test_user_no_users(self):
        self.assertEqual(self.user.noUsers(), 1, msg="Invalid function")

    def test_register(self):
        new_business = {
            "name" : "name",
            "category" :"cat",
            "location" : "location",
            "user_id" : "user_id"
        }
        self.business.registerBusiness(new_business)
        self.assertEqual(len(self.business.getAllBusinesses()), 1)

    def test_update_business(self):
        new_business = {
            "name" : "name",
            "category" :"cat",
            "location" : "location",
            "user_id" : "user_id"
        }
        self.assertTrue(self.business.updateBusiness(new_business, 1))