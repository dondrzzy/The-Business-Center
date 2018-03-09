""" Tests for user endpoints """

import json
from .base_test_case import BaseTestCase

class TestUserEndpoints(BaseTestCase):
    """docs for test user endpoints """

    def test_register_user_fails(self):
        """ test registration failure when there are misssing credentials """
        data = json.dumps(dict(name='test', email='test@gmail.com'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_register_success(self):
        """ docs for testing successful register """
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='1234', confirm_password='1234'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response['message'], 'Account created successfully')

    def test_register_email_unique(self):
        """ docs for testing successful register """
        data = json.dumps(dict(name='test', email='test@gmail.com',
                               password='1234', confirm_password='1234'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_login_fail(self):
        """ docs for testing login failure missing password"""
        data = json.dumps(dict(email='test@gmail.com'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_response['message'], 'password is required')

    def test_login_password_mismatch(self):
        """ test password mismatch """
        data = json.dumps(dict(email='test@gmail.com', password='12345'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])

    def test_login_invalid_user(self):
        """ test password mismatch """
        data = json.dumps(dict(email='test2@gmail.com', password='12345'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertEqual(response.status_code, 400)

    def test_login_success(self):
        """ docs for testing login failure """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])

    def test_password_reset_missing(self):
        """ test for missing fields """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertEqual(json_response["message"], "confirm_password is required")

    def test_resetpassword_wrong_user(self):
        """ tests fails when user's email is not known """
        data = json.dumps(dict(email='tests@gmail.com', password='1234', confirm_password="1234"))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertEqual(json_response["message"], "User not found")

    def test_resetpassword_success(self):
        """ tests successful rest password request """
        data = json.dumps(dict(email='test@gmail.com', password='1234', confirm_password='1234'))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['success'])
        self.assertEqual(json_response["message"], "Password reset successfully")
        self.assertEqual(response.status_code, 200)

    def test_logout_no_token(self):
        """ tests failed logout due to no token """
        response = self.client.get('/api/v1/auth/logout')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertFalse(json_response['token'])
        self.assertEqual(json_response["message"], "Token is missing")

    def test_logout_invalid_token(self):
        """ tests failed logout due to no token """
        response = self.client.get('/api/v1/auth/logout',
                                   headers={'x-access-token':'jvsd'},
                                   content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response['success'])
        self.assertFalse(json_response['token'])
        self.assertEqual(json_response["message"], "Token is invalid")

    def test_logout_success(self):
        """ login user, set token in headers adn logout user """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {'x-access-token':json_response["token"]}
        # logout
        resp = self.client.get('/api/v1/auth/logout',
                                   headers=headers, content_type='application/json')
        json_resp = json.loads(resp.data.decode('utf-8'))
        # try creating business
        _data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        _resp = self.client.post('/api/v1/businesses', data=_data,
                         headers=headers,
                         content_type='application/json')
        _json_resp = json.loads(_resp.data.decode('utf-8'))
        self.assertTrue(json_resp['success'])
        self.assertEqual(json_resp["message"], "Your are logged out")
        self.assertFalse(_json_resp['success'])
        self.assertEqual(_json_resp["message"], "Token is invalid, Please login")

    def test_user_logged_in(self):
        """ test a user who is already logged in """
        data = json.dumps(dict(email='test@gmail.com', password='1234'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    headers={'x-access-token':json_response["token"]},
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertFalse(json_response["success"])
        self.assertEqual(json_response["message"], "Already logged in... Redirecting")
