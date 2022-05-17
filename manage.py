import os
import unittest
from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User, BlogPost

app = create_app('development')

manager = Manager(app) 
Migrate = Migrate(app, db)

manager.add_command('server', Server) 
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, BlogPost=BlogPost)

@manager.command
def test():
  """Run the unit tests."""
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
  manager.run() 