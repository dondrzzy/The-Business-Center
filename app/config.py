# default config

import os
base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_database = 'postgresql://postgres:engneerdon@localhost/tbc_db'

class Config(object):
    """docstring for Initial configs"""
    DEBUG = False
    SECRET_KEY = '\x1er/\x8bwzo\xda"\xf2\x8d\x18\xa7\x176/\xb2\x84\xcc\xad\x0e\xdciS'
    

class DevelopmentConfig(Config):
    """docstring for Development"""
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', Config.SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', postgres_database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """docstring for Testing"""
    DEBUG = True    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', postgres_database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """docstring for production"""
    DEBUG = False

app_configuration = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    Production=ProductionConfig
)