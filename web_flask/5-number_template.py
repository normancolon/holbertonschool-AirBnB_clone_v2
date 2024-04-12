#!/usr/bin/python3
"""
Module to start a Flask web service with multiple routes.
"""

from flask import Flask, render_template

# Creating a Flask application instance
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):

    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):

    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_page(n):

    return render_template("5-number.html", number=n)


# Main guard to ensure the server runs only if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
