""" docstring for testing reviews controller """
import unittest
from app.services.review_service import ReviewService

class TestBusinessController(unittest.TestCase):
    """ docstring for testApp class """
    def setUp(self):
        """ init set up """
        self.review_service = ReviewService()

    def test_invalid_review_bid(self):
        """ testing adding a review to an invalid business """
        r_obj = {
            "text":"Nice"
        }
        res = self.review_service.add_review(r_obj, 'wewe', 2)
        self.assertEqual(res["message"], "Invalid business id")

    def test_no_review(self):
        """ testing trying to submit no review """
        r_obj = {}
        res = self.review_service.add_review(r_obj, '1', 2)
        self.assertFalse(res["success"])
