import json
import urllib.request
from flask import Flask

app = Flask(__name__)
@app.route('/')
def is_it_raining_in_seattle():
    try:
        with urllib.request.urlopen(
                'https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
            is_it_raining_in_seattle = response.read().decode()

        if is_it_raining_in_seattle == "true":
            return "<h1>Yes</h1>"
        else:
            return "<h1>No</h1>"

    except Exception as e:
        return f"An error occurred: {e}", "Server Issues :("