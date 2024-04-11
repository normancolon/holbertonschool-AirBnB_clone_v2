#!/usr/bin/python3
"""
Initializes a Flask web application.

Configured to listen on all network interfaces (0.0.0.0) on port 5000.
It defines two routes:
    - '/' displays 'Hello HBNB!'
    - '/hbnb' displays 'HBNB'
"""

from flask import Flask

# Instantiate the Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display a greeting 'Hello HBNB!' at the application's root."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Respond with 'HBNB' when accessing the '/hbnb' route."""
    return "HBNB"


# Ensure the server runs only if the module is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
