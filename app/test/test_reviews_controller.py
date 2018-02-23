"""docstring for ReviewController"""
import unittest
from app.controllers.review_controller import ReviewController


class TestBusinessController(unittest.TestCase):
    """docstring for TestUser"""
    def setUp(self):
        """docstring for setUp"""
        self.review_controller = ReviewController()

    def test_review_invalid_business(self):
        """docstring for invalid business id"""
        test_review = {"text":"yey"}
        res = self.review_controller.add_review(test_review, 'w')["success"]
        self.assertFalse(res, msg="Invalid reviews function")


    def test_add_review_missing_text(self):
        """docstring for testing missing text"""
        test_review = {}
        res = self.review_controller.add_review(test_review, '2')["msg"]
        self.assertEqual(res, "Provide a review ('text')", msg="Invalid reviews function")

    def test_get_business_reviews(self):
        """docstring for testing business"""
        res = self.review_controller.get_business_reviews('1')["success"]
        self.assertTrue(res, msg="Invalid reviews function")
