#!/usr/bin/python3
"""
This module launches a Flask application that greets users.
Accessible via the root URL, it will simply return a greeting.
Listens on 0.0.0.0 across all interfaces at port 5000.
"""

from flask import Flask

# Initialize the Flask application
greet_app = Flask(__name__)


@greet_app.route("/", strict_slashes=False)
def greet():
    """Responds with 'Hello HBNB!' when accessing the root URL."""
    return "Hello HBNB!"


# Entry point for running the application
if __name__ == "__main__":
    greet_app.run(host="0.0.0.0", port=5000)
