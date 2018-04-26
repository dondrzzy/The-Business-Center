""" docs for app settings """
import os
BD = os.path.abspath(os.path.dirname(__file__))
PDB = 'postgresql://postgres:postgres@localhost/tbc_db'


class Config(object):
    """docstring for Initial configs"""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    BUSINESSES_PER_PAGE = 5
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FRONT_END_URL = 'http://localhost:3000/'


class DevelopmentConfig(Config):
    """docstring for Development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', PDB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """docstring for Testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', PDB+'_test')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """docstring for production"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FRONT_END_URL = 'https://the-business-center.herokuapp.com/'

CONF = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
