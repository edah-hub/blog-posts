from importlib.resources import contents
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
from flask import Flask,render_template,url_for,flash,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] ='4db77598290f06523456cafce29ac3d9'
app.config['SQLAlchemy_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    username = db.Column(db.String(255),unique=True,nullable=False)
    image_file = db.Column(db.String(255),unique=True,nullable=False)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog posts 1',
        'content':'First Post Content',
        'Date Posted': 'April 20th,2015'
    },
        {
        'author': 'Eddy Schoffieldr',
        'title': 'Blog post 2',
        'content':'Second Post Content Post Content',
        'Date Posted': 'April 20th,2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = "about")

@app.route("/contact_us/")
def contact_us():
     return "<h1> Contact us page </h1>"
 
@app.route("/register/")
def register():
    form = RegistrationForm()
    return render_template("register.html",title = "Registration", form=form)

@app.route("/login/")
def login():
    form = LoginForm()
    return render_template("login.html",title = "Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)