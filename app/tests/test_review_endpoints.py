""" tests for review end points """
import json
from .base_test_case import BaseTestCase

class TestReviewsEndpoints(BaseTestCase):
    """docs for test business endpoints """
    def login_get_token(self):
        """login user and return token """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='#user@2017'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        return json.loads(response.data.decode('utf-8'))
    def create_business(self, token):
        """ create business """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':token},
                         content_type='application/json')


    def test_review_missing_token(self):
        """ add review fail, missing token"""
        token = self.login_get_token()["token"]
        # create business
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nicee'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_review_missing_input(self):
        """ add review fail, missing text"""
        token = self.login_get_token()["token"]
        # create business
        self.create_business(token)
        # add review
        data = json.dumps(dict(tcext='nicee'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    headers={'x-access-token':token},
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_review_unknown_business(self):
        """ add review fail, missing text"""
        token = self.login_get_token()["token"]
        # create business
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nicee'))
        response = self.client.post('/api/v1/businesses/109/reviews',
                                    headers={'x-access-token': token},
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_add_review(self):
        """ docs for adding a review successfully"""
        token = self.login_get_token()["token"]
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nice'))
        response = self.client.post('/api/v1/businesses/1/reviews',
                                    data=data, headers={'x-access-token':token},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_business_reviews(self):
        """ test for getting business reviews """
        # login
        token = self.login_get_token()["token"]
        # create business
        self.create_business(token)
        # add review
        data = json.dumps(dict(text='nice'))
        self.client.post('/api/v1/businesses/1/reviews',
                         data=data, headers={'x-access-token':token},
                         content_type='application/json')

        # get reviews
        response = self.client.get('/api/v1/businesses/1/reviews',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
