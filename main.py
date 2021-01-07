import data
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)
@app.route("/")
def home_route():
    return render_template("home.html", projects=data.setup())

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')