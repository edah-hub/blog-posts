from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import BlogPost

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

  def test_createblog(self):
    blogpost = BlogPost(title='love and culture', created_at='', updated_at='', content='hello world', category='music', image_file='default.jpg')
    db.session.add(blogpost)
    self.assertEqual(blogpost.title, 'love and culture')
  
  def test_deleteblog(self):