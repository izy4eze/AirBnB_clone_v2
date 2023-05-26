#!/usr/bin/python3
"""
A script that starts a Flask web application
The web application listens on 0.0.0.0 and port 5000
"""

from flask import Flask

app = Flask("__name__") 

@app.route("airbnb-onepage", strict_slashes = False)
def hello_hbnb():
    """return a string"""
    return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host="0.0.0.0:5000")
