#!/usr/bin/python3
"""
This module initializes a Flask  that serves a list of states from a database on a web page.
"""

from models import storage
from flask import Flask, render_template

# Create the Flask application instance
state_app = Flask(__name__)


@state_app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Render an HTML page that lists all states stored in the database.
    The states are sorted alphabetically by their names.
    """
    # Fetch all states from the database
    state_list = storage.all("State").values()
    sorted_states = sorted(state_list, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@state_app.teardown_appcontext
def cleanup_session(exception=None):
    """
    Clean up the database session at the end of each request to prevent data leakage.
    """
    storage.close()


# Condition to ensure the server
if __name__ == "__main__":
    state_app.run(host="0.0.0.0", port=5000)
