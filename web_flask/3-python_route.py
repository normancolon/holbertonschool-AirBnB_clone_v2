#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Route for the root URL


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

# Route for the /hbnb URL


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

# Route for /c/<text> URL


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')

# Route for /python/<text> URL with a default value for text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
