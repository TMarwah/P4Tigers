from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_login import LoginManager, UserMixin
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy
from custom import error
import requests
import os

# create a Flask instance
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login = LoginManager(app)


# connects default URL of server to render home.html
dbURI = 'sqlite:///' + os.path.join(basedir, 'models/myDB.db')
""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = "qwerty"
db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/api')
def idk():
    response = requests.get('http://aws.random.cat/meow')
    image = response.json()['file']
    return render_template("api.html", image=image)

@app.route('/h')
def index():
    return render_template("database.html")
# Create a sign up page
@app.route('/')
def home_route():
    return render_template("home.html")

@app.route('/index')
def index_route():
    return render_template("index.html")

@app.route('/testimonial')
def testimonial_route():
    return render_template("testmonial.html")
# connects /hello path of server to render hello.html

@app.route('/secret')
def secret_route():
    return render_template("secret.html")
# connects /hello path of server to render hello.html

@app.route('/login', methods=['POST', 'GET'])
def login():
    secretpass = "hello"
    if request.method == "POST":
        # redirects us to the user page
        if request.form.get("password") and request.form.get("confirmation") == secretpass:
            return redirect("/secret")
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    """Register user"""
    if request.method == "POST":
        # Make sure they put in their username
        if not request.form.get("username"):
            return error("must provide username", 1)

        # Make sure they put in a password
        elif not request.form.get("password"):
            return error("must provide password", 2)

        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return error("passwords must match", 3)

        fullname = request.form.get("first") + request.form.get("last")

        # Insert all the values into the database
        db.engine.execute(text("INSERT INTO users (username, hash, name) VALUES (:user, :hash, :name);").execution_options(autocommit=True),
                          user=request.form.get("username"),
                          hash=generate_password_hash(request.form.get("password")),
                          name=fullname)

        return redirect("/login")
    else:
        return render_template("signup.html")

# connects /flask path of server to render flask.html
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == "POST":
        newuser = request.form["newusername"] # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("newuser", newusr=newuser))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def newuser(newuser):
    return f"<h1>{newuser}</h1>"
# Create a sign up page

if __name__ == "__main__":
    db.create_all()
    # runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
