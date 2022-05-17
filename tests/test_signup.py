from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User


class UserModelCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app('test')
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()
  
  def test_signup(self):
    user = User(username='test_user', email='test@gmail.com', password='123456')
    db.session.add(user)
    self.assertEqual(user.email, 'test@gmail.com')