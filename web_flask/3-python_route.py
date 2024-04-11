#!/usr/bin/python3
"""
Initializes a Flask web server that is accessible on 0.0.0.0, listening on port 5000.
Routes handle various paths and display corresponding messages.
"""

from flask import Flask

# Create an instance of the Flask class
application = Flask(__name__)


@application.route("/", strict_slashes=False)
def greet():
    """Respond with 'Hello HBNB!' at the root."""
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Return the string 'HBNB' when accessing the /hbnb route."""
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def show_c_text(text):
    """Return 'C ' followed by the modified user input, changing underscores to spaces."""
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@application.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@application.route("/python/<text>", strict_slashes=False)
def show_python_text(text):
    """Display 'Python' followed by the user-provided text, with default text if none provided.

    Underscores in the text are replaced with spaces.
    """
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


# Run the Flask application if the script is executed directly
if __name__ == "__main__":
    application.run(host="0.0.0.0")
