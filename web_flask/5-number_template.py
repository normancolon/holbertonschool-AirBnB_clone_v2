#!/usr/bin/python3
from flask import Flask, render_template

server = Flask(__name__)


@server.route('/')
def root():
    return 'Hello HBNB!'


@server.route('/hbnb')
def hbnb():
    return 'HBNB'


@server.route('/c/<text>')
def show_c(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@server.route('/python/', defaults={'text': 'is cool'})
@server.route('/python/<text>')
def show_python(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@server.route('/number/<int:n>')
def number(n):
    return f'{n} is a number'


@server.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)
