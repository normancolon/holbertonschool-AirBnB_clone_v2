#!/usr/bin/python3
"""
Flask web application that dynamically displays the list of states and associated cities
from a database, available at 0.0.0.0 on port 5000.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Renders an HTML page that lists all states with their cities sorted alphabetically.
    Each state's cities are displayed as a sublist under the state's name.
    """
    states = {state.id: state for state in sorted(
        storage.all("State").values(), key=lambda x: x.name)}
    for state in states.values():
        state.cities = sorted(state.cities, key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states.values())


@app.teardown_appcontext
def close_session(exception=None):
    """
    Closes the database session at the end of the request to ensure that resources are freed and
    the connection to the database is not left open.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
