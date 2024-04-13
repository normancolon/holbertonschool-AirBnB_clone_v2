#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': "is cool"})
@app.route("/python/<text>")
def python_text(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number_n(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template_n(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even_n(n):
    odd_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", number=n, odd_even=odd_even)


@app.route("/states_list")
def states_list():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states")
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(err=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
