""" Tests for user endpoints """

import json
from .base_test_case import BaseTestCase

class TestUserEndpoints(BaseTestCase):
    """docs for test user endpoints """
    @staticmethod
    def get_new_user():
        """ generates json data for an unregistered user"""
        return json.dumps(dict(name='test', email='test1@gmail.com',
                               password='#user@2017', confirm_password='#user@2017'))
    @staticmethod
    def get_auth_user():
        """ generates json data for an authenticated user"""
        return json.dumps(dict(name='test', email='test@gmail.com', password='#user@2017',
                               confirm_password='#user@2017'))

    def test_register_user_fails(self):
        """ test registration failure when there are misssing credentials """
        data = json.dumps(dict(name='test', email='test@gmail.com'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_register_wrong_name(self):
        """ test registration failure when name is invalid """
        data = json.dumps(dict(name='test@3', email='test@gmail.com'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_register_wrong_email(self):
        """ test registration failure when email is invalid """
        data = json.dumps(dict(name='test', email='test'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_weak_password(self):
        """ test registration failure the password is weak """
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='1234', confirm_password='1234'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_password_mismatch(self):
        """ test registration failure the passwords do not match """
        data = json.dumps(dict(name='test', email='test1@gmail.com',
                               password='#user@2018', confirm_password='#user@20019'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_long_email_fail(self):
        """ test registration failure when email address exceeds allowed db value """
        email = 'testtesttesttesttesttesttesttesttesttesttesttestttesttestttesttestttes \
                 ttestttesttestttesttestttesttestttesttestttesttestttesttest@gmail.com'
        data = json.dumps(dict(name='test', email=email,
                               password='#user@2017', confirm_password='#user@2017'))
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_register_success(self):
        """ docs for testing successful register """
        data = self.get_new_user()
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_email_unique(self):
        """ docs for testing unsuccessful register due to identical emails """
        data = self.get_auth_user()
        response = self.client.post('/api/v1/auth/register', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_login_fail(self):
        """ docs for testing login failure missing password"""
        data = json.dumps(dict(email='test@gmail.com'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_login_password_mismatch(self):
        """ test password mismatch """
        data = json.dumps(dict(email='test@gmail.com', password='#user@2018'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_login_invalid_user(self):
        """ login fail due to unregistered user """
        data = json.dumps(dict(email='test2@gmail.com', password='#user@2018'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_login_success(self):
        """ docs for testing login failure """
        data = json.dumps(dict(email='test@gmail.com', password='#user@2017'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_relogin_fail(self):
        """ docs for testing login failure """
        data = self.get_auth_user()
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {'x-access-token':json_response["token"]}
        response = self.client.post('/api/v1/auth/login', data=data,
                                    headers=headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_doublelogin_fail(self):
        """ docs for testing login failure """
        data = self.get_auth_user()
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {'x-access-token':json_response["token"]}
        data = json.dumps(dict(email='test1@gmail.com', password='#user@2017'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    headers=headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_password_reset_missing(self):
        """ test for missing fields when resetting password """
        data = json.dumps(dict(email='test@gmail.com', password='#user@2017'))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_resetpassword_wrong_user(self):
        """ tests fails when user's email is not known """
        data = json.dumps(dict(email='tests@gmail.com', password='#user@2017',
                               confirm_password="#user@2017"))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_resetpassword_success(self):
        """ tests successful rest password request """
        data = json.dumps(dict(email='test@gmail.com', password='#user@2017',
                               confirm_password='#user@2017'))
        response = self.client.post('/api/v1/auth/reset-password',
                                    data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_logout_no_token(self):
        """ tests failed logout due to no token """
        response = self.client.get('/api/v1/auth/logout')
        self.assertEqual(response.status_code, 401)

    def test_logout_invalid_token(self):
        """ tests failed logout due to no token """
        response = self.client.get('/api/v1/auth/logout',
                                   headers={'x-access-token':'jvsd'},
                                   content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_logout_success(self):
        """ login user, set token in headers adn logout user """
        data = self.get_auth_user()
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        headers = {'x-access-token':json_response["token"]}
        # logout
        self.client.get('/api/v1/auth/logout',
                        headers=headers, content_type='application/json')
        # try creating business
        business_data = json.dumps(dict(name="Business", category="IT", location="Kampala"))
        business_resp = self.client.post('/api/v1/businesses', data=business_data,
                                         headers=headers, content_type='application/json')
        self.assertEqual(business_resp.status_code, 401)

    def test_user_logged_in(self):
        """ test a user who is already logged in """
        data = self.get_auth_user()
        response = self.client.post('/api/v1/auth/login', data=data,
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        response = self.client.post('/api/v1/auth/login', data=data,
                                    headers={'x-access-token':json_response["token"]},
                                    content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
