#!/usr/bin/python3
"""
Initializes a Flask app to display states from a database.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Render states sorted alphabetically by their names.
    """
    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def cleanup_session(exception=None):
    """
    Close the database session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
