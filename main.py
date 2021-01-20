from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from custom import error

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render home.html
dbURI = 'sqlite:///models/myDB.db'
""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)


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


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["username"]  # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("user", usr=user))
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
    # runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')
