#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_check(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
