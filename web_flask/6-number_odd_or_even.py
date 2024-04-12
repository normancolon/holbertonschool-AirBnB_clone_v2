#!/usr/bin/python3
"""
This script initiates a Flask application designed to respond to various URL paths
with text or HTML responses, showcasing basic dynamic content handling.
The server is configured to listen on all network interfaces (0.0.0.0) using port 5000.
"""

from flask import Flask, render_template

# Flask application instance creation
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Returns a simple greeting message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a short message for the '/hbnb' route."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_message(text):
    """Displays 'C' followed by the text argument, spaces replacing underscores."""
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_message(text):
    """Displays 'Python' followed by the text argument or the default."""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Confirms that 'n' is an integer."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page with the number if 'n' is an integer."""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Displays an HTML page that states if 'n' is odd or even."""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)


# Conditional main for running the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
