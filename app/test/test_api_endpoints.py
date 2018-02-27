import unittest
from flask.ext.testing import TestCase
from app import app, db
from app.config import app_configuration
from app.schemas import User
import json
import sys


class BaseTestCase(TestCase):
    """ A base test case """
    def create_app(self):
        app.config.from_object(app_configuration['testing'])
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User('test', 'test@gmail.com', '1234'))
        db.session.commit()

    def tearDown(self):
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
        data = json.dumps(dict(name='test', email='test1@gmail.com', password='1234', password_c='1234'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/register', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])

    def test_register_email_unique(self):
        """ docs for testing successful register """
        data = json.dumps(dict(name='test', email='test@gmail.com', password='1234', password_c='1234'))
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
        self.assertEqual(json_response['msg'], 'password is required')

    def test_login_success(self):
        """ docs for testing login failure """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        content_type = 'application/json'
        response = self.client.post('/api/v1/auth/login', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])

    def test_token_required_create_business(self):
        """ docs for testing create business fail if not logged in """
        data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        content_type = 'application/json'
        response = self.client.post('/api/v1/businesses', data=data, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertFalse(json_response['token'])

    def test_business_missing_attributes(self):
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
        response = self.client.post('/api/v1/businesses', data=data, headers=headers, content_type=content_type)
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])


