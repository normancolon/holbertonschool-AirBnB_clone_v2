#!/usr/bin/python3
"""
Initializes a Flask web server that is accessible on 0.0.0.0 and listens on port 5000.
This server handles various routes to display corresponding messages.
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
    """
    Return the string 'HBNB' when accessing the /hbnb route.
    Returns:
        str: 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c_text(text):
    """
    Return 'C ' followed by the user input with underscores replaced by spaces.
    Args:
        text (str): The path variable provided by the user.
    Returns:
        str: Formatted string with 'C ' prefix.
    """
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python_text(text):
    """
    Display 'Python' followed by the provided text, with a default if none is provided.
    Underscores in the text are replaced with spaces.
    Args:
        text (str): The text to display after 'Python'.
    Returns:
        str: Complete greeting with Python.
    """
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


# Condition to run the Flask app only if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
