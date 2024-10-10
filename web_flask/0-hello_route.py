#!/usr/bin/env python3
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for '/' that displays "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Run the application only if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)