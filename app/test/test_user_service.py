""" docstring for test user controller test """
import unittest
from app.services.user_service import UserService


class TestUserController(unittest.TestCase):
    """ docstring for testApp class """
    def setUp(self):
        """ init set up """
        self.user_service = UserService()

    def test_user_registration_no_name(self):
        """testing user registration """
        test_user = {
            "email":"test@gmail.com",
            "password":"1234",
            "confirm_password":"1234"
        }
        res = self.user_service.register_user(test_user)
        expected_res = {"success":False, "message":"name is required"}
        self.assertEqual(res, expected_res, msg="Registration method faulty")

    def test_login_missing(self):
        """tests for mising inputs when user logs in"""
        test_user = {
            "password":"1234"
        }
        res = self.user_service.login_user(test_user)
        self.assertFalse(res["success"])

    def test_login_error_res(self):
        """tests for mising inputs error responses"""
        test_user = {
            "email":"test@gmail.com"
        }
        res = self.user_service.login_user(test_user)
        self.assertEqual(res["message"], "password is required")

    def test_reset_pwd_mistmatch(self):
        """ test of password mismatch """
        test_user = {
            "email":"unkown@gmail.com",
            "password":"1234",
            "confirm_password":"124"
        }
        res = self.user_service.reset_password(test_user)
        self.assertFalse(res["success"])
