""" docstring for testing reviews controller """
import unittest
from app.controllers.review_controller import ReviewController

class TestBusinessController(unittest.TestCase):
    """ docstring for testApp class """
    def setUp(self):
        """ init set up """
        self.review_controller = ReviewController()

    def test_invalid_review_bid(self):
        """ testing adding a review to an invalid business """
        r_obj = {
            "text":"Nice"
        }
        res = self.review_controller.add_review(r_obj, 'wewe', 2)
        self.assertEqual(res["msg"], "Invalid business id")

    def test_no_review(self):
        """ testing adding a review to an invalid business """
        r_obj = {
            
        }
        res = self.review_controller.add_review(r_obj, '1', 2)
        self.assertFalse(res["success"])
