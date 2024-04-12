#!/usr/bin/python3
import sys
from flask import Flask, render_template
from models import storage, State, Amenity

sys.path.append('/home/lol/holbertonschool-AirBnB_clone_v2/')
webapp = Flask(__name__, static_url_path='/static', static_folder='static')


@webapp.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


@webapp.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@webapp.route('/c/<text>', strict_slashes=False)
def c_route(text="is cool"):
    return 'C ' + text.replace('_', ' ')


@webapp.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@webapp.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return 'Python ' + text.replace('_', ' ')


@webapp.route('/number/<n>', strict_slashes=False)
def number_route(n):
    return f'{n} is a number' if n.isdigit() else '404 not found'


@webapp.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n) if n.isdigit() else '404 not found'


@webapp.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    if n.isdigit():
        type_num = 'even' if int(n) % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', number=int(n), number_type=type_num)
    return '404 not found'


@webapp.route('/states_list', strict_slashes=False)
def states_list():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@webapp.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=states)


@webapp.route('/states', strict_slashes=False)
@webapp.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all(State).values()
    if id:
        state = next((s for s in states if s.id == id), None)
        return render_template('9-states.html', state=state) if state else 'Not Found', 404
    return render_template('9-states.html', states=states)


@webapp.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@webapp.teardown_appcontext
def close_session(exception=None):
    storage.close()


if __name__ == '__main__':
    webapp.run(host='0.0.0.0', port=5000)
