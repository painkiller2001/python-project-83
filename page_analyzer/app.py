from flask import Flask, render_template
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# @app.route("/")
# def first_hello_func():
#     return f'Hello, man!'


@app.get("/")
def get_main_content():
    return render_template(
        'index.html'
        )