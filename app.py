from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>/<int:birth_year>")
def greet(name, birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return f"<p>Hi {name}, you are {age} years old.</p>"
