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

	# def test_initial_model_id(self):
	# 	self.assertEqual(self.my_users.id, 0, msg='Account Balance Invlalid')

	# def test_initial_user(self):
	# 	self.assertEqual(len(self.my_users.users), 1, msg='No initial User set')

	# def test_user_registration(self):
	# 	new_user = {
	# 		"name" : "Don",
	# 		"email" : "test2@gmail.com",
	# 		"password" : "1234",
	# 		"password_c" : "1234"
	# 	}
	# 	self.my_users.register(new_user)
	# 	self.assertEqual(len(self.my_users.users), 2, msg='User was not registered')

	# def test_login(self):
	# 	new_user = {
	# 		"name" : "Don",
	# 		"email" : "test2@gmail.com",
	# 		"password" : "1234",
	# 		"password_c" : "1234"
	# 	}
	# 	self.my_users.register(new_user)
	# 	self.assertEqual(len(self.my_users.users), 2, msg='User was not registered')
	# 	login_user = {
	# 		"email" : "test2@gmail.com",
	# 		"password" : "1234"
	# 	}
	# 	self.assertEqual(self.my_users.login(login_user), {"success":True, "pwd":True}, msg='Login failed')

	# def test_get_users(self):
	# 	number_types = (int,  float, complex)
	# 	res = self.my_users.noUsers()
	# 	print(res)
	# 	self.assertTrue(isinstance(res, number_types), msg='get users doesnot return an number')

if __name__ == '__main__':
	unittest.main()
