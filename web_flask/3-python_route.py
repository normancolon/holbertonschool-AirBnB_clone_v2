#!/usr/bin/python3
"""
Initializes a Flask web server that is accessible
"""

from flask import Flask

# Create an instance of the Flask class to initiate the application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    Respond with 'Hello HBNB!' at the root URL.
    Returns:
        str: Greeting message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c_text(text):

    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python_text(text):

    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
