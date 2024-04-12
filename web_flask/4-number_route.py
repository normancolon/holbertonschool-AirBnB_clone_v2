#!/usr/bin/python3
"""
This module launches a Flask application simple text content on different routes.
"""

from flask import Flask

# Instantiate the Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):

    modified_text = text.replace("_", " ")
    return f"C {modified_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):

    modified_text = text.replace("_", " ")
    return f"Python {modified_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_check(n):

    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
