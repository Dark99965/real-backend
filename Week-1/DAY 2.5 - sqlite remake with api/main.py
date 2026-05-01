
# imports

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# app

app = Flask(__name__)

# home route

@app.route('/')
def home():
    return render_template("home.html")

# app runer

if __name__ == '__main__':
    app.run(debug=True)