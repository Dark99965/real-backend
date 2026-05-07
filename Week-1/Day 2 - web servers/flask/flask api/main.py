# imports

from flask import Flask, render_template

# Flask app

app = Flask(__name__)

# home route

@app.route("/")
def home():
    return render_template("home.html")

# debuging stuff

if __name__ == '__main__':
    app.run(debug=True)