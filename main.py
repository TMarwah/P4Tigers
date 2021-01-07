import data  # projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render home.html


# Create a sign up page
@app.route('/')
def home_route():
    return render_template("home.html", projects=data.setup())


# connects /hello path of server to render hello.html


@app.route('/proj/')
def hello_route():
    return render_template("5hr.html", projects=data.setup())


@app.route('/anim/')
def animation_route():
    return render_template("animation.html", projects=data.setup())


# connects /flask path of server to render flask.html


@app.route('/playlist/')
def playlist_route():
    return render_template("playlist.html", datalist=data.playlist(), projects=data.setup())

# Create a sign up page

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
