from flask import Flask, render_template, request, redirect, flash
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


url_base = [
    {
        "id": 1,
        "url": "https://www.hexlet.io"
    },
    {
        "id": 2,
        "url": "https://www.google.com"
    },
    {
        "id": 3,
        "url": "https://www.youtobe.com"
    }         
]

# @app.route("/")
# def first_hello_func():
#     return f'Hello, man!'


@app.get("/")
def get_main_content():
    return render_template(
        'index.html'
        )


@app.get("/urls")
def get_url_list():

    sorted_data = sorted(url_base, key=lambda x: x['id'], reverse=True)

    

    return render_template(
        'urls/url_list.html',
        urls=sorted_data
        )


@app.get("/url/<int:url_id>")
def get_url_by_id(url_id):
    
    url = next((url['url'] for url in url_base if url['id'] == url_id), None)

    if url is None:
        error = 'URL is missing!'
        return render_template(
            'urls/url_by_id.html',
            error=error
        ), 404

    return render_template(
        'urls/url_by_id.html',
        url=url,
        url_id=url_id
    )
    


# @app.post("/")
# def get_url():
#     url = request.form.to_dict()
#     return render_template(
#         url=url
#         )