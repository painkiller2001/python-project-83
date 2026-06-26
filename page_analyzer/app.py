from flask import Flask


app = Flask(__name__)


@app.route("/")
def first_hello_func():
    return f'Hello, man!'
