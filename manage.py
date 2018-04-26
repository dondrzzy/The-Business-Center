# import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.models.user import User
from app.models.business import Business
from app.models.review import Review
from app.models.token import Token

from app.config import CONF

ENV = os.getenv("ENVIRON", 'testing')
app.config.from_object(CONF[ENV])
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """ Run tests without coverage """
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()


