from flask import session
class User(object):
	"""docstring for User"""
	def __init__(self, id = 0, users = [{"id":1, "name":"Sibo", "email":"test@gmail.com", "password":"1234"}]):
		self.users = users
		self.id = id


	
	def register(self, _user):
		for user in self.users:
			if _user["email"] == user["email"]:
				print('found')
				return False

		new_user = {
			"id" : len(self.users)+1,
			"name" : _user["name"],
			"email" : _user["email"],
			"password" : _user["password"] 
		}
		self.users.append(new_user)	
		return  True

	def login(self, _user):
		for user in self.users:
			if user["email"] == _user["email"]:
				if user["password"] == _user["password"]:
					session["id"] = user["id"]
					return {"success":True, "pwd":True}
				return {"success":True, "pwd":False}

		return {"success":False, "pwd":False}

	def getUsers(self):
		return self.users

	def noUsers(self):
		return len(self.users)

	def resetPassword(self, _user):
		for user in self.users:
			if _user["email"] == user["email"]:
				user["password"] = _user["password"]
				return True
		return False