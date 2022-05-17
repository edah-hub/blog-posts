from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
# from flask_simplemde import SimpleMDE
from config import config_options

db = SQLAlchemy() #instance of the db
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()
# simple = SimpleMDE()

 

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config_options[config_name])

  #intializing extensions
  db.init_app(app)
  login_manager.init_app(app)
  bcrypt.init_app(app)
  mail.init_app(app)
  # simple.init_app(app)

  #Registering blueprints
  from .main import main
  app.register_blueprint(main)

  
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  return app