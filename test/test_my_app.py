import unittest
from app.controllers.business_controller import BusinessController
from app.controllers.user_controller import UserController

 
class TestApp(unittest.TestCase):
    def setUp(self):
        self.user_controller = UserController()

    def test_user_registration_no_name(self):
        test_user={
            "email":"test@gmail.com",
            "password":"1234",
            "password_c":"1234"
        }
        self.assertEqual(self.user_controller.register_user(test_user), {"success":False, "msg":"name is required"}, msg="Registration method faulty")


if __name__ == '__main__':
    unittest.main()
