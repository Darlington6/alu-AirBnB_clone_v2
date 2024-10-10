#!/usr/bin/python3
""" Web application listening on 0.0.0.0, port 5000 """
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask # type: ignore
>>>>>>> af4bc8895922a24786b7976dfb79415ca172aad7

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/",strict_slashes = False)
=======
@app.route("/", strict_slashes = False)
>>>>>>> af4bc8895922a24786b7976dfb79415ca172aad7
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000)
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> af4bc8895922a24786b7976dfb79415ca172aad7
