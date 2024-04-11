#!/usr/bin/python3
"""
This module initiates a Flask web application that serves two types of HTML pages:
- One that displays a list of all state objects from the database,
- Another that displays details for a specific state identified by its ID.
The application is accessible from all network interfaces on port 5000.
"""

from models import storage
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """
    Serve a webpage that lists all state objects from the database.
    States are presented in alphabetical order by their names.
    """
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template("9-states.html", states=states, id=None)


@app.route("/states/<string:id>", strict_slashes=False)
def get_state_by_id(id):
    """
    Serve a webpage that shows details about a state specified by its 'id', if it exists.
    """
    state = storage.get("State", id)
    if state:
        return render_template("9-states.html", states=[state], id=id)
    return render_template("9-states.html", id="Not found")


@app.teardown_appcontext
def teardown_db_session(exception):
    """
    This function is called after each request, ensuring that the database session is closed.
    This is crucial for freeing up resources that were temporarily allocated during the request.
    """
    storage.close()


# Run the Flask app only if this script is executed directly (i.e., not imported).
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
