# server set up
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return { "message": "Welcome to my project!"}


if __name__ == '__name__':
    app.run(debug=True)