#!/usr/bin/python3
from models.state import State
from models import storage
from flask import Flask, render_template
import sys
# Append a specified directory to sys.path for module importation
sys.path.append(
    '/home/lol/holbertonschool-AirBnB_clone_v2/web_flask/static/images')

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the string 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):
    """ Returns 'C' and the text with spaces instead of underscores. """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    """ Returns 'Python' and the text with spaces instead of underscores. """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def int_display(n):
    """ Returns message if n is a number. """
    if n.isdigit():
        return f'{n} is a number'
    return '404 not found'


@app.route('/number_template/<n>', strict_slashes=False)
def display_number(n):
    """ Renders a page showing n if n is a digit. """
    if n.isdigit():
        return render_template('5-number.html', number=n)
    return '404 not found'


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def display_even_odd(n):
    """ Renders a page stating if n is even or odd if n is a digit. """
    if n.isdigit():
        n = int(n)
        number_type = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', number=n, number_type=number_type)
    return '404 not found'


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ Displays sorted list of states. """
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
