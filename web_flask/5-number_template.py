#!/usr/bin/python3
from flask import Flask, render_template

# Flask app setup
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    """Greet at root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Show 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text="is cool"):
    """Display 'C <text>'"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    """Display 'Python <text>'"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def show_number(n):
    """Validate number"""
    if n.isdigit():
        return f'{n} is a number'
    return '404 not found'


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
