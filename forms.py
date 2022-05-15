import email
from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ConfirmField,SubmitField,BooleanField
from wtforms import DataRequired,Length,Email,EqualTo

class Registration (FlaskForm):
    username = StringField('username',validators=[DataRequired,Length(min = 2,max = 20)])
    email = StringField('Email',validators=[DataRequired,Email()])
    password = PasswordField('Password',validators=[DataRequired,password_option])
    confirm = ConfirmField('Confirm Password',validators=[DataRequired,EqualTo('password')])
    submit = SubmitField('Submit')
    
class Login (FlaskForm):
    username = StringField('username',validators=[DataRequired,Length(min = 2,max = 20)])
    email = StringField('Email',validators=[DataRequired,Email()])
    password = PasswordField('Password',validators=[DataRequired,password_option])
    rememberMe = BooleanField('Remember')
    submit = SubmitField('Submit')