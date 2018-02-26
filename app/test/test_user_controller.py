""" docstring for test user controller test """
import unittest
from app.controllers.user_controller import UserController


class TestUserController(unittest.TestCase):
    """ docstring for testApp class """
    def setUp(self):
        """ init set up """
        self.user_controller = UserController()

    def test_user_registration_no_name(self):
        """testing user registration """
        test_user = {
            "email":"test@gmail.com",
            "password":"1234",
            "password_c":"1234"
        }
        res = self.user_controller.register_user(test_user)
        epx_res = {"success":False, "msg":"name is required"}
        self.assertEqual(res, epx_res, msg="Registration method faulty")

    def test_login_missing(self):
        """tests for mising inputs"""
        test_user = {
            "password":"1234"
        }
        res = self.user_controller.login_user(test_user)
        self.assertFalse(res["success"])

    def test_login_error_res(self):
        """tests for mising inputs error responses"""
        test_user = {
            "email":"test@gmail.com"
        }
        res = self.user_controller.login_user(test_user)
        self.assertEqual(res["msg"], "password is required")

    def test_reset_password(self):
        """ tests for unknown user resetting password """
        test_user = {
            "email":"unkown@gmail.com",
            "password":"1234",
            "password_c":"1234"
        }
        res = self.user_controller.reset_password(test_user)
        self.assertEqual(res["msg"], "User not found")

    def test_reset_pwd_mistmatch(self):
        """ test of password mismatch """
        test_user = {
            "email":"unkown@gmail.com",
            "password":"1234",
            "password_c":"124"
        }
        res = self.user_controller.reset_password(test_user)
        self.assertFalse(res["success"])
