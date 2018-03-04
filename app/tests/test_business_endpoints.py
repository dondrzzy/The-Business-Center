""" tests for business endpoint """
import json
from .base_test_case import BaseTestCase

class TestBusinessEndpoints(BaseTestCase):
    """docs for test business endpoints """
    def test_business_token_required(self):
        """ docs for testing create business fail if not logged in """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        response = self.client.post('/api/v1/businesses', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_business_attributes(self):
        """ tests for missing business credentials """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        response = self.client.post('/api/v1/businesses', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_create_business(self):
        """ docs for testing create business succcess """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        res = self.client.post('/api/v1/businesses', data=data,
                               headers={'x-access-token':json_response["token"]},
                               content_type='application/json')
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_res['success'])

    def test_get_zero_business(self):
        """ docs for testing get all businesses, no businesses currently"""
        response = self.client.get('/api/v1/businesses', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(len(json_response['businesses']), 0)

    def test_get_all_business(self):
        """ docs for testing get all businesses, no businesses currently"""
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # get all businesses
        response = self.client.get('/api/v1/businesses', content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(len(json_response['businesses']), 1)

    def test_get_invalid_business_fail(self):
        """ docs for testing getting invalid business """
        response = self.client.get('/api/v1/businesses/hfhfh')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertEqual(json_response['message'], "Invalid business id")

    def test_get_unknown_business_fail(self):
        """ docs for testing getting invalid business """
        response = self.client.get('/api/v1/businesses/9')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertEqual(json_response['message'], "Business with id 9 not found")

    def test_get_single_business(self):
        """docs for getting a business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # get single business
        response = self.client.get('/api/v1/businesses/1')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response['business']['id'], 1)

    def test_update_business(self):
        """ docs for updating business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # update business
        new_data = json.dumps(dict(name='Business', category='Accounts', location='Kampala'))
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers={'x-access-token':json_response["token"]},
                              content_type='application/json')
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_res['success'])
        self.assertEqual(json_res['business']['category'], 'Accounts')

    def test_update_unknown_business(self):
        """ docs for updating business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # update business
        new_data = json.dumps(dict(name='Business', category='Accounts', location='Kampala'))
        res = self.client.put('/api/v1/businesses/9', data=new_data,
                              headers={'x-access-token':json_response["token"]},
                              content_type='application/json')
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertFalse(json_res['success'])
        self.assertEqual(json_res['message'], "Business with id 9 not found")

    def test_unauth_update_business(self):
        """ docs for updating business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # logout
        response = self.client.get('/api/v1/auth/logout',
                                   headers={'x-access-token':json_response["token"]},
                                   content_type='application/json')
        # register
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='1234', confirm_password='1234'))
        self.client.post('/api/v1/auth/register', data=data, content_type='application/json')
        # login
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # update business
        new_data = json.dumps(dict(name='Business', category='Accounts', location='Kampala'))
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers={'x-access-token':json_response["token"]},
                              content_type='application/json')
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertFalse(json_res['success'])
        self.assertEqual(json_res['message'], "You can not perform that action")

    def test_delete_business(self):
        """ docs for deleting business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        business_data = json.dumps(dict(name="MyBusiness", category="ICT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=business_data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # delete it
        resp = self.client.delete('/api/v1/businesses/1',
                                  headers={'x-access-token':json_response["token"]},
                                  content_type='application/json')
        json_resp = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])

    def test_delete_business_auth(self):
        """ docs for deleting business """
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # create business
        business_data = json.dumps(dict(name="MyBusiness", category="ICT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=business_data,
                         headers={'x-access-token':json_response["token"]},
                         content_type='application/json')
        # logout
        response = self.client.get('/api/v1/auth/logout',
                                   headers={'x-access-token':json_response["token"]},
                                   content_type='application/json')
        # register
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='1234', confirm_password='1234'))
        self.client.post('/api/v1/auth/register', data=data, content_type='application/json')
        # login
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        # delete it
        resp = self.client.delete('/api/v1/businesses/1',
                                  headers={'x-access-token':json_response["token"]},
                                  content_type='application/json')
        json_resp = json.loads(resp.data.decode('utf-8'))
        self.assertFalse(json_resp['success'])
        self.assertEqual(json_resp['message'], "You can not perform that action")
