#!/usr/bin/python3
"""
Flask application initializer module.

This application is configured to listen on all network interfaces (0.0.0.0) using port 5000.
It includes two routes:
    - '/' which displays 'Hello HBNB!'
    - '/hbnb' which displays 'HBNB'
"""

from flask import Flask

# Creating an instance of the Flask class to initiate the application
web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def display_hello():
    """Returns a greeting to the client by displaying 'Hello HBNB!'."""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Returns 'HBNB' as a response to the client."""
    return "HBNB"


# Run the application if this script is executed as the main program
if __name__ == "__main__":
    web_app.run(host="0.0.0.0")
