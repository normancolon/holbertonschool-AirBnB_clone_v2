#!/usr/bin/python3
from flask import Flask, render_template, abort

app = Flask(__name__)


def sanitize_text(text):

    return text.replace('_', ' ')


@app.route('/', strict_slashes=False)
def hello_hbnb():

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):

    return f"C {sanitize_text(text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):

    return f"Python {sanitize_text(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_display(n):

    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number(n):

    return render_template('5-number.html', number=n)


@app.errorhandler(404)
def not_found(error):

    return "This route is not available. Please check your URL.", 404


if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)),
            debug=os.getenv('DEBUG', False) == 'True')
