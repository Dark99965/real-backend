# imports

from enum import unique

from flask import Flask, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

# Flask app

app = Flask(__name__)

# data base

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TODO: make usr module

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)

# home route

@app.route("/")
def home():
    return render_template("home.html")

# api route

@app.route('/api')
def api():
    resp = make_response(jsonify({"msg": "Hello, world!"}))
    resp.access_control_allow_origin = '*'
    return resp

# debuging stuff

if __name__ == '__main__':
    app.run(debug=True)