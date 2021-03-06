""" tests for business endpoint """
from app.services.business_service import BusinessService
from .base_test_case import BaseTestCase
BS = BusinessService()

class TestAppErrorHandling(BaseTestCase):
    """Testing application general custom error message """

    def test_unknown_endpont(self):
        """ test for unknown route"""
        response = self.client.get('/api/s2/businesses')
        self.assertIn(b'requested URL was not found on the server', response.data)
        self.assert404(response)

    def test_method_not_allowed(self):
        """ test for an invalid method to a route """
        response = self.client.get('/api/v1/auth/register')
        self.assertIn(b'Method Not Allowed', response.data)
        self.assert405(response)
