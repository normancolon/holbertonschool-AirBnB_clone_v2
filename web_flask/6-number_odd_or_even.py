#!/usr/bin/python3
"""
Launches a Flask web service with various routes on port 5000.
It responds with plain text and HTML pages based on route-specific logic.
"""

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)
# Configure Jinja2 environment to automatically strip blocks
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def greet():
    """Respond with a simple greeting."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show_hbnb():
    """Return the string 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """Return 'C' followed by the custom text, replacing underscores with spaces."""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    """Return 'Python ' followed by the custom text, underscores replaced with spaces."""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """Display a message that confirms the input is a number."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Render an HTML page that shows the number, only if it's an integer."""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Render an HTML page that indicates whether a number is odd or even."""
    context = {
        'number': n,
        'parity': 'even' if n % 2 == 0 else 'odd'
    }
    return render_template("6-number_odd_or_even.html", **context)


# Condition to ensure the script runs only when executed, not when imported
if __name__ == "__main__":
    app.run(host="0.0.0.0")
