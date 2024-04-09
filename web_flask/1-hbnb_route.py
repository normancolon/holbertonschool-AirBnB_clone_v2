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


if __name__ == "__main__":
    # Run the app on all interfaces (0.0.0.0) and port 5000
    app.run(host="0.0.0.0", port=5000)
