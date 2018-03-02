# import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.user import User
from app.models.business import Business
from app.models.review import Review
from app.models.token import Token

from app import app, db
from app.config import CONF

# ENV = os.getenv("ENVIRON", 'testing')
app.config.from_object(CONF['development'])
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


