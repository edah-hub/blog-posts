from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class NewPost(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])
  category = SelectField('Category', choices=[('music','Music'), ('fashion','Fashion'), ('entertainment','Entertainment'), ('art','Art'), ('workout','Workout'), ('health','Health')], validators=[DataRequired()])
  image_file =FileField('Upload Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
  submit = SubmitField('Post')


class CommentForm(FlaskForm):
	content = TextAreaField('Add comment', validators=[DataRequired()])
	submit = SubmitField('Post')


