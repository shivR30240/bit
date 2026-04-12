from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Indore from gang 3!</p>"


@app.route("/<name>")
def greet(name):
    return f"<p>Hi, {name}!</p>"
