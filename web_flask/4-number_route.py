#!/usr/bin/python3
"""
This module launches a Flask application that serves simple text content on different routes.
It is accessible on all network interfaces on port 5000.
"""

from flask import Flask

# Instantiate the Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Return a greeting at the application root.
    Returns:
        str: Greeting message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """
    Return a string for the /hbnb route.
    Returns:
        str: 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """
    Return 'C' followed by custom text, replacing underscores with spaces.
    Args:
        text (str): The text to display after 'C'.
    Returns:
        str: Formatted string with 'C ' prefix.
    """
    modified_text = text.replace("_", " ")
    return f"C {modified_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    """
    Return 'Python ' followed by custom text, which defaults to 'is cool'.
    Any underscores in the text will be replaced with spaces.
    Args:
        text (str): The text to display after 'Python'.
    Returns:
        str: Complete greeting with Python.
    """
    modified_text = text.replace("_", " ")
    return f"Python {modified_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_check(n):
    """
    Display the number with a message if the route parameter is a valid integer.
    Args:
        n (int): Number to display.
    Returns:
        str: Message stating the number is a number.
    """
    return f"{n} is a number"


# Ensure the server runs only if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
