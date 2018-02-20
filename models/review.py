import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath('reviews.py'))
sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(os.path.dirname(CURRENT_DIR+'\\models\\reviews.py'))
print(sys.path)

from flask import session
from business import Business

business = Business()

class Review(object):
	
	def __init__(self, reviews=[]):
		self.reviews = reviews


	def addReview(self, rev, bid):	
		print(business.getBusiness(bid))
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

