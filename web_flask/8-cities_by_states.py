#!/usr/bin/python3
import sys
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


sys.path.append('/home/lol/holbertonschool-AirBnB_clone_v2/')

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def greet():
    return 'Hello HBNB!'


@web_app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    return 'HBNB'


@web_app.route('/c/<text>', strict_slashes=False)
def display_c(text="is cool"):
    clean_text = text.replace('_', ' ')
    return f"C {clean_text}"


@web_app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@web_app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    clean_text = text.replace('_', ' ')
    return f"Python {clean_text}"


@web_app.route('/number/<n>', strict_slashes=False)
def number(n):
    return f'{n} is a number' if n.isdigit() else '404 not found'


@web_app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n) if n.isdigit() else '404 not found'


@web_app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    if n.isdigit():
        parity = 'even' if int(n) % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', number=n, parity=parity)
    return '404 not found'


@web_app.route('/states_list', strict_slashes=False)
def list_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@web_app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
