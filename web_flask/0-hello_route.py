#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Define the route for '/' with strict_slashes set to False
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    # The app will listen on all interfaces on port 5000
    app.run(host="0.0.0.0", port=5000)
