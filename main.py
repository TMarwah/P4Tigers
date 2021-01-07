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


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')