import secrets
import os
from flask import current_app
from PIL import Image


def save_blog_picture(form_picture):
  random_hex = secrets.token_hex(8) 
  _, f_ext = os.path.splitext(form_picture.filename) 
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(current_app.root_path, 'static/images/blog_pictures', picture_fn ) 
  uploaded_image = Image.open(form_picture) 
  uploaded_image.save(picture_path) 
  return picture_fn 