#!/usr/bin/python3
"""
Initializes a Flask web server  routes configured.
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    Responds to the root URL ("/") with a greeting.
    Returns:
        A string "Hello HBNB!" as a greeting.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """
    Responds to the URL "/hbnb" with a string.
    Returns:
        The string "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c_text(text):

    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


# Run the Flask app if this file is executed directly (not imported)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
