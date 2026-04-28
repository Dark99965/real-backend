# imports

from flask import Flask
from flask import render_template
from flask import request
import sqlite3
# app

app = Flask(__name__)

# home route

@app.route('/')
def home():
    email = request.args.get("email")
    passwd = request.args.get("passwd")
    if email and passwd:
        conn = sqlite3.connect("app.db")
        curser = conn.cursor()
        curser.execute(f"insert into users values (?, ?)", (email, passwd))
        conn.commit()
        conn.close()
    return render_template("index.html")