from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import Comment

class BlogPostModelCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app('test')
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_comment(self):
    comment = Comment(content='love and culture', created_at='', updated_at='')
    db.session.add(comment)
    self.assertEqual(comment.content, 'love and culture')