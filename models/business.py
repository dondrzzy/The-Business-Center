class Business(object):
	def __init__(self, businesses = []):
		self.businesses = businesses

	def registerBusiness(self, b):
		new_business = {
			"id" : len(self.businesses) + 1,
			"name" : b["name"],
			"category" : b["category"],
			"location" : b["location"],
			"user_id" : b["user_id"]
		}
		self.businesses.append(new_business)
		return True
	
	def getAllBusinesses(self):
		return self.businesses

	def getBusiness(self, bid):
		for b in self.businesses:
			if b["id"] == bid:
				return {'found':True, "business":b}
		return {'found':False, "business":{}}

	def updateBusiness(self, _b, bid):

		for b in self.businesses:
			if b["id"] == bid:
				if "name" in _b:
					b["name"] = _b["name"]
				if "category" in _b:
					b["category"] = _b["category"]
				if "location" in _b:
					b["location"] = _b["location"]
				return True
		return False

	def deleteBusiness(self, bid):
		for b in self.businesses:
			if b["id"] == bid:
				self.businesses.remove(b)
				return True
		return False

		
