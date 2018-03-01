""" docs for testing api module """
import json
from passlib.hash import sha256_crypt
from flask.ext.testing import TestCase
from app import app, db
from app.config import CONF
from app.models.user import User
from app.models.business import Business




class BaseTestCase(TestCase):
    """ A base test case """
    def create_app(self):
        """ docs for creating the app """
        app.config.from_object(CONF['testing'])
        return app

    def setUp(self):
        """ docs for docstring """
        db.create_all()
        db.session.add(User(name='test', email='test@gmail.com', password=sha256_crypt.encrypt(str('1234'))))
        # db.session.add(Business(user_id=1, name='Business', category='Accounts', location='Mbarara'))
        db.session.commit()

    def tearDown(self):
        """ docs for deleting the database method """
        db.session.remove()
        db.drop_all()

class TestApiEndpoints(BaseTestCase):
    """docs for test API endpoints """
    def test_register_user_fails(self):
        """ test registration failure when there are misssing credentials """
        data = json.dumps(dict(name='test', email='test@gmail.com'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/register', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_register_success(self):
        """ docs for testing successful register """
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='1234', confirm_password='1234'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/register', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response['message'], 'Account created successfully')

    def test_register_email_unique(self):
        """ docs for testing successful register """
        data = json.dumps(dict(name='test', email='test@gmail.com',
                               password='1234', confirm_password='1234'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/register', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_login_fail(self):
        """ docs for testing login failure """
        data = json.dumps(dict(email='test@gmail.com'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_response['message'], 'password is required')

    def test_login_success(self):
        """ docs for testing login failure """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])

    def test_business_token_required(self):
        """ docs for testing create business fail if not logged in """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        content_type = 'application/json'
        response = self.client.post('/api/v1/businesses', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_business_attributes(self):
        """ tests for missing business credentials """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        content_type = 'application/json'
        response = self.client.post('/api/v1/businesses', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_create_business(self):
        """ docs for testing create business succcess """
        content_type = 'application/json'
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        res = self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_res['success'])

    def test_get_all_business(self):
        """ docs for testing get all businesses, no businesses currently"""
        content_type = 'application/json'
        response = self.client.get('/api/v1/businesses', content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(len(json_response['businesses']), 0)

    def test_get_all_business(self):
        """ docs for testing get all businesses, no businesses currently"""
        content_type = 'application/json'
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        # get all businesses
        response = self.client.get('/api/v1/businesses', content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(len(json_response['businesses']), 1)

    def test_get_invalid_business_fail(self):
        """ docs for testing getting invalid business """
        response = self.client.get('/api/v1/businesses/hfhfh')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_get_single_business(self):
        """docs for getting a business """
        content_type = 'application/json'
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        # get single business
        response = self.client.get('/api/v1/businesses/1')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response['business']['id'], 1)

    def test_update_business(self):
        """ docs for updating business """
        content_type = 'application/json'
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        # update business
        new_data = json.dumps(dict(name='Business', category='Accounts', location='Kampala'))
        res = self.client.put('/api/v1/businesses/1', data=new_data,
                              headers=headers, content_type=content_type)
        json_res = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_res['success'])
        self.assertEqual(json_res['business']['category'], 'Accounts')

    def test_delete_business(self):
        """ docs for deleting business """
        # login
        content_type = 'application/json'
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        business_data = json.dumps(dict(name="MyBusiness", category="ICT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=business_data,
                         headers=headers, content_type=content_type)
        # delete it
        resp = self.client.delete('/api/v1/businesses/1', headers=headers,
                                  content_type=content_type)
        json_resp = json.loads(resp.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])

    def test_add_review_fail(self):
        """ docs for adding a review successfully"""
        content_type = 'application/json'
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        # add review
        data = json.dumps(dict(text='nice'))
        response = self.client.post('/api/v1/businesses/1/reviews', data=data, content_type=content_type)
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_resp['message'], 'Token is missing')
    def test_add_review(self):
        """ docs for adding a review successfully"""
        content_type = 'application/json'
        # login
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {
            'x-access-token':json_response["token"]
        }
        # create business
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        self.client.post('/api/v1/businesses', data=data,
                               headers=headers, content_type=content_type)
        # add review
        data = json.dumps(dict(text='nice'))
        response = self.client.post('/api/v1/businesses/1/reviews', data=data, headers=headers, content_type=content_type)
        json_resp = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])
