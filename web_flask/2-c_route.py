#!/usr/bin/python3
"""
Initializes a Flask web server with specific routes configured.
This server is accessible on all network interfaces (0.0.0.0) and listens on port 5000.
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
    """
    Displays 'C' followed by the user-provided text.
    Args:
        text (str): The text provided by the user via the URL.
    Returns:
        A string starting with 'C' followed by the text, where underscores are replaced with spaces.
    """
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


# Run the Flask app if this file is executed directly (not imported)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
