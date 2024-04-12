#!/usr/bin/python3


from flask import Flask, render_template

# Flask application instance creation
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_message(text):

    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_message(text):

    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Confirms that 'n' is an integer."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):

    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):

    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
