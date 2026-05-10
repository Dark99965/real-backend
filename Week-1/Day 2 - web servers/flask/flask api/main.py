# imports

from flask import Flask, render_template, jsonify, make_response

# Flask app

app = Flask(__name__)

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