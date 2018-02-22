import unittest
from app.models.user import UserModel
 
class TestApp(unittest.TestCase):
	def setUp(self):
		self.user = UserModel()

	def test_model_is_member(self):
		res = self.user.is_member({"email":"no_email"})
		self.assertEqual(res["success"], False, msg="Is Member function is not working")

	def test_model_reset_password(self):
		self.assertFalse(self.user.reset_password({"email":"123"})["success"], msg="Method should return false")


if __name__ == '__main__':
	unittest.main()
