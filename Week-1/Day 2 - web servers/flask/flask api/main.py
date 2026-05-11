# imports

from flask import Flask, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

# Flask app

app = Flask(__name__)

# data base

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///app.db'

db = SQLAlchemy(app)

# home route

@app.route("/")
def home():
    return render_template("home.html")

# api route

@app.route('/api')
def api():
    resp = make_response(jsonify({"msg": "Hello, world!"}))
    resp.access_control_allow_origin = 'http://localhost:5000/'
    return resp

# debuging stuff

if __name__ == '__main__':
    app.run(debug=True)