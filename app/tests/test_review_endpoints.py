""" tests for review end points """
import json
from .base_test_case import BaseTestCase

class TestReviewsEndpoints(BaseTestCase):
    """docs for test business endpoints """
    def login_get_token(self):
        """login user and return token """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        return json.loads(response.data.decode('utf-8'))
    def create_business(self, token):
        """ create business """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':token},
                         content_type='application/json')


    def test_add_review_fail(self):
        """ docs for adding a review successfully"""
        token = self.login_get_token()["token"]
        # create business
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nicee'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    data=data, content_type='application/json')
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_resp['message'], 'Token is missing')

    def test_add_review(self):
        """ docs for adding a review successfully"""
        token = self.login_get_token()["token"]
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nice'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    data=data, headers={'x-access-token':token},
                                    content_type='application/json')
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])

    def test_get_business_reviews(self):
        """ test for getting business reviews """
        # login
        token = self.login_get_token()["token"]
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nice'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    data=data, headers={'x-access-token':token},
                                    content_type='application/json')
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])

        # get reviews
        response = self.client.get('/api/v1/businesses/1/reviews',
                                   headers={'x-access-token':token},
                                   content_type='application/json')
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])
        self.assertIn(b'nice', response.data)
