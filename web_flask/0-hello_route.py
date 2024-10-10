#!/usr/bin/python3
""" Web application listening on 0.0.0.0, port 5000 """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
<<<<<<< HEAD
    app.url_map.strict_slashes = False
=======
    app.url_map.strict_slashes = False

>>>>>>> 9bcb7f831f881b3aa5220fd8fc2e494f27320f6e
