import sys
import math
import os
from flask import Flask, escape, request, render_template, flash
import json
import requests
from requests.exceptions import HTTPError
from flask_bootstrap import Bootstrap
from conf import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)

with open('config.json') as j:
        conf = json.load(j)

@app.route('/')
def index():
        user = {'username': 'Arthur'}
        return render_template('index.html', title='Home', user=user)
        

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
    # include some validation on the search input
    searchtype = 'search'
    query = request.form['title']
    #if query.validate_on_submit():
    #    flash('Search cannot be blank')
    print(query)
    if searchtype == 'search': param = 's'
    url = "http://www.omdbapi.com/?apikey=815bb1ac&{}={}".format(param,query)
    x = requests.get(url)
    results = json.loads(x.text)
    results = results['Search']
    print(type(results))
    
    return render_template('search_results.html', title=query, searchResults=results) #f'Hello, you searched for {movie_title} by {movie_director}!' # this should actually go to the search results page template

@app.route('/movie/<movie_imdbID>')
def movie_detail(movie_imdbID):
    """if fetch data from movie database by oid and display info."""
    #qs_name = request.args.get('name', '')
    #qs_oid = request.args.get('oid', '')
    param = 'i'
    query = movie_imdbID
    print("IMDB ID: ",query)
    url = "http://www.omdbapi.com/?apikey=815bb1ac&{}={}".format(param,query)
    x = requests.get(url)
    results = json.loads(x.text)
    title = results['Title']
    #print('Results: ', results)
    return render_template('movie.html', title=title, movieSelect=results) #f'Hello, {escape(name)}!'

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))        # look into alternate ways to do this?
        app.run(host='0.0.0.0', port=port)



