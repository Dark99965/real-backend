# imports

from flask import Flask, render_template, jsonify

# Flask app

app = Flask(__name__)

# home route

@app.route("/")
def home():
    return render_template("home.html")

# api route

@app.route('/api')
def api():
    return jsonify({ "msg": "Hello, world"})

# debuging stuff

if __name__ == '__main__':
    app.run(debug=True)