from flask import session
from .business import Business

class Review(Business):
	
	def __init__(self, reviews=[]):
		self.reviews = reviews


	def addReview(self, rev, bid):	
		print(self.getBusiness(bid))
		new_rev = {
			"id" : len(self.reviews)+1,
			"businessId" : bid,
			"userId" : session["id"],
			"text" : rev["text"]
		}
		self.reviews.append(new_rev)
		return True

	def getAllReviews(self):
		return self.reviews

	def getBusinessReviews(self, bid):
		output = []
		for r in self.reviews:
			if r["businessId"] == bid:
				output.append(r)
		return output

