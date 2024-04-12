#!/usr/bin/python3
"""
Module to start a Flask web service with multiple routes.
Host: 0.0.0.0, Port: 5000
Provides text and HTML responses based on path and dynamic content.
"""

from flask import Flask, render_template

# Creating a Flask application instance
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """Returns a greeting as plain text at the application root."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Returns the string 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Returns 'C' followed by the custom text, spaces replace underscores."""
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Returns 'Python' followed by the custom text; default is 'is cool'.

    Spaces replace underscores in the text.
    """
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """Displays a string indicating the integer value provided."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_page(n):
    """Renders an HTML page if an integer is provided, using a template."""
    return render_template("5-number.html", number=n)


# Main guard to ensure the server runs only if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
