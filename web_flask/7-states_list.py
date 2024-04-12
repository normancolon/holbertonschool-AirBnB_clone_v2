#!/usr/bin/python3
"""
Flask web application that lists all states from the database.
Accessible at http://0.0.0.0:5000/states_list
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders an HTML page that lists all states from the database, sorted by name."""
    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db_session(exception):
    """Closes the database session at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
