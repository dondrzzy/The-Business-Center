""" tests for business endpoint """
import json
from .base_test_case import BaseTestCase

class TestBusinessEndpoints(BaseTestCase):
    """docs for test business endpoints """

    @staticmethod
    def get_registered_user():
        """ generates json data for a registered user"""
        return json.dumps(dict(email='test@gmail.com', password='#user@2017'))

    @staticmethod
    def get_unregistered_user():
        """ generates json data for an unregistered user"""
        return json.dumps(dict(name='test', email='test1@gmail.com',
                               password='#user@2017', confirm_password='#user@2017'))

    @staticmethod
    def get_business():
        """ generates json data for an unregistered business"""
        return json.dumps(dict(name="Business", category="IT", location="Kampala"))

    def login_test_user(self):
        """ login test user"""
        data = self.get_registered_user()
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        return json.loads(response.data.decode('utf-8'))["token"]

    def create_test_business(self, token):
        """ create business for testing endpoints """
        data = self.get_business()
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':token},
                         content_type='application/json')

    def test_business_token_required(self):
        """ docs for testing create business fail if not logged in """
        data = self.get_business()
        response = self.client.post('/api/v1/businesses', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_business_attributes(self):
        """ tests for missing business credentials """
        token = self.login_test_user()
        data = json.dumps(dict(name="Business", category="IT"))
        response = self.client.post('/api/v1/businesses', data=data,
                                    content_type='application/json',
                                    headers={'x-access-token':token})
        self.assertEqual(response.status_code, 422)

    def test_invalid_business_input(self):
        """ assert false when business input is invalid"""
        token = self.login_test_user()
        data = json.dumps(dict(name="123", category="#$%$", location="*(7722"))
        response = self.client.post('/api/v1/businesses', data=data,
                                    content_type='application/json',
                                    headers={'x-access-token':token})
        self.assertEqual(response.status_code, 422)


    def test_create_business(self):
        """ docs for testing create business succcess """
        token = self.login_test_user()
        # create business
        data = self.get_business()
        res = self.client.post('/api/v1/businesses', data=data,
                               headers={'x-access-token':token},
                               content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_zero_business(self):
        """ docs for testing get all businesses, no businesses currently"""
        response = self.client.get('/api/v1/businesses', content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_get_all_business(self):
        """ docs for testing get all businesses, no businesses currently"""

        # get current number of businesses
        initial_response = self.client.get('/api/v1/businesses', content_type='application/json')
        intial_json = json.loads(initial_response.data.decode('utf-8'))
        intial_length = len(intial_json['businesses'])
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # get all businesses
        response = self.client.get('/api/v1/businesses', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(json_response['businesses']), intial_length+1)


    def test_pagination(self):
        """ test whether result is paginated """
        token = self.login_test_user()
        self.create_test_business(token)
        response = self.client.get('/api/v1/businesses')
        self.assertIn(b'next_page', response.data)

    def test_user_business(self):
        """ testing get user's businesses """
        token = self.login_test_user()
        self.create_test_business(token)
        url = '/api/v1/users/businesses?q=Business&category=IT&location=Kampala'
        response = self.client.get(url, headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_business_fail(self):
        """ docs for testing getting invalid business """
        response = self.client.get('/api/v1/businesses/hfhfh')
        self.assertEqual(response.status_code, 400)

    def test_get_unknown_business_fail(self):
        """ docs for testing getting invalid business """
        response = self.client.get('/api/v1/businesses/99')
        self.assertEqual(response.status_code, 404)

    def test_get_single_business(self):
        """docs for getting a business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # get single business
        response = self.client.get('/api/v1/businesses/1')
        self.assertEqual(response.status_code, 200)

    def test_update_business(self):
        """ docs for updating business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # update business
        new_data = self.get_business()
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers={'x-access-token':token},
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_update_missing_input(self):
        """ test update business fail due to missing input """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # update business
        new_data = json.dumps(dict(name="Business", category="IT"))
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers={'x-access-token':token},
                              content_type='application/json')
        self.assertEqual(res.status_code, 422)

    def test_update_unknown_business(self):
        """ docs for updating business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # update business
        new_data = self.get_business()
        res = self.client.put('/api/v1/businesses/9', data=new_data,
                              headers={'x-access-token':token},
                              content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_unauth_update_business(self):
        """ docs for updating business with no authority """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # logout
        self.client.get('/api/v1/auth/logout',
                        headers={'x-access-token':token},
                        content_type='application/json')
        # register
        data = self.get_unregistered_user()
        self.client.post('/api/v1/auth/register', data=data, content_type='application/json')
        # login
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # update business
        new_data = self.get_business()
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers={'x-access-token':json_response["token"]},
                              content_type='application/json')
        self.assertEqual(res.status_code, 401)

    def test_delete_business(self):
        """ docs for deleting business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # delete it
        res = self.client.delete('/api/v1/businesses/1',
                                 headers={'x-access-token':token},
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_delete_unknown_business(self):
        """ docs for deleting an unknown business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # delete it
        res = self.client.delete('/api/v1/businesses/109',
                                 headers={'x-access-token':token},
                                 content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_delete_business_auth(self):
        """ docs for deleting business """
        # login
        token = self.login_test_user()
        # create business
        self.create_test_business(token)
        # logout
        response = self.client.get('/api/v1/auth/logout',
                                   headers={'x-access-token':token},
                                   content_type='application/json')
        # register
        data = self.get_unregistered_user()
        self.client.post('/api/v1/auth/register', data=data, content_type='application/json')
        # login
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # delete it
        res = self.client.delete('/api/v1/businesses/1',
                                 headers={'x-access-token':json_response["token"]},
                                 content_type='application/json')
        self.assertEqual(res.status_code, 401)
