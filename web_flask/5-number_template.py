#!/usr/bin/python3
"""
This module initiates a Flask application with diverse routing and dynamic content rendering capabilities.
It operates on host 0.0.0.0 and port 5000, offering both text and HTML responses based on the request path.
"""

from flask import Flask, render_template

# Instantiate the Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """
    Returns a greeting message at the root URL.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns the string 'HBNB' at the specified route.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Returns a string starting with 'C' followed by user-defined text.
    Underscores in the text are replaced with spaces.
    """
    return "C " + text.replace("_", " ")


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by user-defined text or the default 'is cool'.
    Underscores are replaced with spaces.
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Confirms if the provided path variable is an integer by displaying 'n is a number'.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page from a template if the path variable is an integer,
    displaying the number within an H1 tag.
    """
    return render_template('5-number.html', number=n)


# Ensures that the server is started only when this script is executed directly
if __name__ == "__main__":
    # Enable debug for development purposes
    app.run(host="0.0.0.0", debug=True)
