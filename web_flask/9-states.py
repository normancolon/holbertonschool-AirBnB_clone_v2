#!/usr/bin/python3
"""
Initializes a Flask web application that serves HTML pages for viewing the details of states
and their respective cities from a database. The application listens on all interfaces
on port 5000.
"""

from models import storage
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """
    Renders a webpage listing all states stored in the database, sorted alphabetically by name.
    """
    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    return render_template("9-states.html", states=states, id=None)


@app.route("/states/<string:id>", strict_slashes=False)
def state_detail(id):
    """
    Renders a detailed webpage for a specific state identified by 'id'. If the state does not
    exist, renders a "Not found" page.
    """
    state = storage.get("State", id)
    if state:
        return render_template("9-states.html", states=[state], id=id)
    else:
        return render_template("9-states.html", id="Not found")


@app.teardown_appcontext
def teardown(exception=None):
    """
    Closes the database session at the end of each request to prevent memory leaks
    and keep the application's performance stable.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
