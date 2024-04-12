#!/usr/bin/python3
'''
Flask application with multiple routes.
Utilizes ORM for displaying states.
'''
from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Returns 'Hello HBNB!' at the root. '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Returns 'HBNB'. '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):
    ''' Returns 'C ' followed by the text with spaces. '''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    ''' Returns 'Python ' followed by the text. '''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_display(n):
    ''' Displays if n is an integer. '''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number(n):
    ''' Renders a page displaying the integer n. '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_even_odd(n):
    ''' Displays if n is odd or even in HTML. '''
    return render_template('6-number_odd_or_even.html', number=n, number_type='even' if n % 2 == 0 else 'odd')


@app.route('/states_list', strict_slashes=False)
def display_states():
    ''' Displays all states sorted by name. '''
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    ''' Closes the database session after request. '''
    storage.close()


if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=environ.get('PORT', 5000),
            debug=environ.get('DEBUG', False) == 'True')
