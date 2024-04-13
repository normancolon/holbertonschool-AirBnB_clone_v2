#!/usr/bin/python3
import sys
from flask import Flask, render_template, abort
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    """Display a greeting message."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """Display 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text="is cool"):

    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):

    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):

    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):

    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):

    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all states sorted by name."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():

    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
