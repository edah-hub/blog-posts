from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, current_user, logout_user, login_required, login_user
from app.models import User, BlogPost, Comment
from .forms import RegistrationForm, LoginForm
from app import bcrypt, db
from . import auth


@auth.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))

  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email = form.email.data, password = hashed_password)
    db.session.add(user)
    db.session.commit()
    user_email = user.email

    flash(f'Hello { form.username.data}, Your Account was created succesfully! You are now able to log in', 'success')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', title='Register', form=form)

@auth.route('/login',  methods=['GET', 'POST'])
def login():

  if current_user.is_authenticated:
    return redirect('main.index')
  
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.index'))   
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')

  return render_template('auth/login.html', title='Login', form=form)




@auth.route('/logout')
def logout():
  logout_user()
  return redirect (url_for('main.index'))

