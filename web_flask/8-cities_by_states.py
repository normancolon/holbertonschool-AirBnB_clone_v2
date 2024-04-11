#!/usr/bin/python3
"""
Initializes a Flask web application intended to display a list of all states
and their cities from a storage backend. The application is accessible on all
network interfaces on port 5000.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_states_and_cities():
    """
    Serve an HTML page that lists all states and their associated cities
    from the database, sorted by state names and then city names.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


@app.teardown_appcontext
def cleanup_db_session(exception=None):
    """
    Ensures that the database session is properly closed after each request,
    preventing data leakage and keeping the application's resource usage efficient.
    """
    storage.close()


# Ensure that the Flask application runs only if it's the main module executed.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
