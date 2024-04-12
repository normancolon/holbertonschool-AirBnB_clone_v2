#!/usr/bin/python3
import sys
from flask import Flask, render_template
from models import storage
from models.state import State

sys.path.append('/home/lol/holbertonschool-AirBnB_clone_v2/')
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def int_display(n):
    return f'{n} is a number' if n.isdigit() else '404 not found'


@app.route('/number_template/<n>', strict_slashes=False)
def display_number(n):
    return render_template('5-number.html', number=n) if n.isdigit() else '404 not found'


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def display_even_odd(n):
    if n.isdigit():
        n = int(n)
        number_type = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', number=n, number_type=number_type)
    return '404 not found'


@app.route('/states_list', strict_slashes=False)
def display_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
