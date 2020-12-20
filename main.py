from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', project="Individual Mastery Week 9")

@app.route('/main')
def main():
    stocks = [
        {
            "name":"Qualcomm",
            "price":145.01,
            "divyield":1.79
        },

        {
            "name":"Nvidia",
            "price":582.48,
            "divyield":.11
        },
    ]
    return render_template("main.html", stocks=stocks)

@app.route('/bio')
def bio():
    embed = "https://repl.it/@BraydenBasinger"
    return render_template("bio.html", age=True)

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')