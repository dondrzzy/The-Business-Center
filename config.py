import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Common configurations

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '12345678'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:engneerdon@localhost/tbc_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SECRET_KEY = '12345678'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:engneerdon@localhost/tbc_db'

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = True
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}