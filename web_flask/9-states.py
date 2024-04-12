#!/usr/bin/python3
from models.city import City
from models.state import State
from models import storage
from flask import Flask, render_template
import sys
sys.path.append(
    '/home/lol/holbertonschool-AirBnB_clone_v2/web_flask/static/images')

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


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def find_state(id=None):
    states = storage.all(State).values()
    if id:
        state = next((state for state in states if state.id == id), None)
        return render_template('9-states.html', state=state) if state else "Not Found"
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
