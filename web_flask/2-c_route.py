#!/usr/bin/python3
"""
Initializes a Flask web server with specific routes.
Serves on 0.0.0.0 and listens on port 5000.
"""

from flask import Flask

# Initialize the Flask application
application = Flask(__name__)

# Route definitions


@application.route("/", strict_slashes=False)
def greet():
    """Returns a greeting."""
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Returns 'HBNB'."""
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def show_c_text(text):
    """Displays 'C' followed by the user-provided text, spaces replace underscores."""
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


# Main executable
if __name__ == "__main__":
    application.run(host="0.0.0.0")
