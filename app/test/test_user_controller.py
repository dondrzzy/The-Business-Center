"""docstring for ReviewController"""
import unittest
from app.controllers.user_controller import UserController


class TestUserController(unittest.TestCase):
    """docstring for TestUser"""
    def setUp(self):
        """docstring for set up"""
        self.user_controller = UserController()

    def test_register_mising_info(self):
        """docstring for testing missing register info"""
        test_user = {"id":1, "name":"Sibo", "email":"test@gmail.com", "password":"1234"}
        res = self.user_controller.register_user(test_user)["success"]
        self.assertFalse(res, msg="Invalid register user function")

    # test if it denies identical emails
    def test_email_exists(self):
        """docstring for testing initial user email"""
        test_user = {
            "id":1, "name":"Sibo", "email":"test@gmail.com",
            "password":"1234", "password_c":"1234"
        }
        res = self.user_controller.register_user(test_user)["success"]
        self.assertFalse(res, msg="Error, enique email failure")

    def test_user_register_success(self):
        """docstring for testing register success"""
        test_user = {
            "id":1, "name":"Sibo", "email":"test1@gmail.com",
            "password":"1234", "password_c":"1234"
        }
        res = self.user_controller.register_user(test_user)
        self.assertTrue(res, msg="User registration failed")

    def test_user_login_no_password(self):
        """docstring for testing user login with no password"""
        test_user = {"email":"test1@gmail.com"}
        res = self.user_controller.login_user(test_user)["success"]
        self.assertFalse(res, msg="Invalid login user function")

    def test_user_login_no_email(self):
        """docstring for testing login with no email"""
        test_user = {"password":"1234"}
        res = self.user_controller.login_user(test_user)["success"]
        self.assertFalse(res, msg="Invalid login user function")

    def test_missing_credentials(self):
        """docstring for testingg reseting password required"""
        test_user = {"email":"test@gmail.com", "password":"1234"}
        res = self.user_controller.reset_password(test_user)["success"]
        self.assertFalse(res, msg="Invalid reset password function")

    def test_reset_password_mismatch(self):
        """docstring for testing user resetting pwd with pwd mismatch"""
        test_user = {"email":"test@gmail.com", "password":"1234", "password_c":"123"}
        res = self.user_controller.reset_password(test_user)["success"]
        self.assertFalse(res, msg="Invalid reset password function")

    def test_reset_pwd_invalid_user(self):
        """docstring for testing invalid user trying to rest pwd"""
        test_user = {"email":"testing@gmail.com", "password":"1234", "password_c":"1234"}
        res = self.user_controller.reset_password(test_user)["msg"]
        self.assertEqual(res, "User not found", msg="Invalid reset password function")
