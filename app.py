import sys
import math
import os
from flask import Flask, escape, request, render_template
import json
import requests
from requests.exceptions import HTTPError
import conf


app = Flask(__name__)

@app.route('/')
def index():
        user = {'username': 'Arthur'}
        test = conf.Conf['test']
        movie_results = [
                {
                        'movietitle': {'movie': 'Waking Life'},
                        'director': {'director': 'Richard Linklater'}
                },
                {
                        'movietitle': {'movie': 'Wonder Woman'},
                        'director': {'director': 'Patty Jenkins'}
                }
        ]
        return render_template('index.html', title='Home', user=user, movie_results=movie_results, test=test)
        

# @app.route('favorites')
# def favorites():
#     #Read out favorited movies.
#     filename = os.path.join('data.json')
#     with open(filename) as data_file:
#         data = json.load(data_file)
#         return data

@app.route('/favorites')
def favorites():
    """if query params are passed, write movie to json file."""
    return render_template('favorites.html')

@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    #x = requests.get('http://www.omdbapi.com/?apikey=815bb1ac&t=')
    query = request.form['title']
    return f'Hello, {query}!'

# @app.route('/movie/<movie_oid>')
# def movie_detail():
#     """if fetch data from movie database by oid and display info."""
#     qs_name = request.args.get('name', '')
#     qs_oid = request.args.get('oid', '')
#     return f'Hello, {escape(name)}!'

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))        # look into alternate ways to do this?
        app.run(host='0.0.0.0', port=port)



