""" docs for testing api module """
from passlib.hash import sha256_crypt
from flask.ext.testing import TestCase
from app import app, db
from app.config import CONF
from app.models.user import User




class BaseTestCase(TestCase):
    """ A base test case """
    @staticmethod
    def create_app():
        """ docs for creating the app """
        app.config.from_object(CONF['testing'])
        return app

    @staticmethod
    def setUp():
        """ docs for docstring """
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.add(User(name='test', email='test@gmail.com',
                            password=sha256_crypt.encrypt(str('1234'))))
        db.session.commit()

    @staticmethod
    def tearDown():
        """ docs for deleting the database method """
        db.session.remove()
        db.drop_all()
