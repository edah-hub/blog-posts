from . import db
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader 
def load_user(user_id):
  return User.query.get(int(user_id)) 

class User(db.Model, UserMixin): 

  __tablename__='users'

  id = db.Column(db.Integer, primary_key = True) 
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable =False)
  password = db.Column(db.String(120), nullable =False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  blog_posts = db.relationship('BlogPost', backref = 'author', lazy='dynamic')
  comments  = db.relationship('Comment', backref='author', lazy='dynamic')

  def __repr__(self):
    return(f"User('{self.username}', '{self.email}')")

class BlogPost(db.Model):

  __tablename__='blogposts'
  
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(200), nullable = False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  category = db.Column(db.String(200), nullable = False)
  image_file = db.Column(db.String(120), nullable =True, default='default.jpg')
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  comments = db.relationship('Comment', backref='blog_post', cascade='all, delete-orphan', lazy='dynamic')


class Comment(db.Model):

  __tablename__='comments'

  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  blogpost_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'), nullable=False)

class Quotes:

  def __init__(self, id, author, quote):
    self.id = id
    self.author = author
    self.quote = quote

