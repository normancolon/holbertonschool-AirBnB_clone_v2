#!/usr/bin/python3
"""
Initializes a Flask web application that serves a dynamic HTML page
for Homebnb's filters feature. The application is accessible on all
network interfaces on port 5000.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    """
    Serve the Homebnb filters page, dynamically populated with states
    and amenities available in the database.
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                           states=sorted(states, key=lambda state: state.name),
                           amenities=sorted(amenities, key=lambda amenity: amenity.name))


@app.teardown_appcontext
def close_db_session(exception=None):
    """
    Clean up the database session after each request to ensure there
    are no lingering connections or transaction issues.
    """
    storage.close()


# The application will only run if it is executed as the main program.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
