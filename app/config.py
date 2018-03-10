""" docs for app settings """
import os
BD = os.path.abspath(os.path.dirname(__file__))
PDB = 'postgresql://postgres:engneerdon@localhost/tbc_db'
HDB = 'postgres://fhdizlfioazvye:158df7e8e77540d8b65b4bce2cc3773aa6ef2e5a7675305fa855da9c53c6508a \
        @ec2-54-225-249-161.compute-1.amazonaws.com:5432/dcsv4cj7150243'

class Config(object):
    """docstring for Initial configs"""
    DEBUG = False
    SECRET_KEY = '\x1er/\x8bwzo\xda"\xf2\x8d\x18\xa7\x176/\xb2\x84\xcc\xad\x0e\xdciS'
    BUSINESSES_PER_PAGE = 4


class DevelopmentConfig(Config):
    """docstring for Development"""
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', Config.SECRET_KEY)
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
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', HDB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

CONF = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
