#!/usr/bin/python3
"""
This Flask web application initializes the Homebnb filters page. It listens
on all network interfaces (0.0.0.0) and serves dynamic content on port 5000.
It pulls state and amenity data from a database to populate the filters.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Display the Homebnb filters page using data from the storage.
    This includes lists of states and amenities sorted alphabetically.
    """
    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    amenities = sorted(storage.all("Amenity").values(),
                       key=lambda amenity: amenity.name)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Close the database session to clean up after each request.
    This prevents leftover database connections or transaction problems.
    """
    storage.close()


# Ensure this script runs only if it is executed as the main module.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
