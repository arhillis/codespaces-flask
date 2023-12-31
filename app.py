from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/about")
def about():
    return "All about me!!!"
