#!/usr/bin/python3
"""Starts a flask application, and defines a single route.

Listening on host 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """handle requests for the root route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def main_hbnb():
    """handle requests for the hbnb route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
