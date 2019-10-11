from app import app
import sys
import math
import os
from flask import Flask, escape, request, render_template, flash
import json
import requests
from requests.exceptions import HTTPError
from flask_bootstrap import Bootstrap
from conf import Config, Conf, Favs
import conf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

@app.route('/')
def index():
        # Home page
        user = {'username': 'Arthur'}
        return render_template('index.html', title='Home', user=user)
        

@app.route('/favorites')
def readfavorites():
        # Read out favorited movies.
        filename = os.path.join("data.json")
        with open(filename) as data_file:
                fav_list = json.load(data_file)
                fav_list = fav_list["favorites"]

        # Load api key from Heroku enviornmental variable
        APPID = os.environ.get('OMDB_API_KEY')
        param = "i" # this is an omdb parameter to retrive by movie ID
        movielist = []
        for movie in fav_list:
                url = "http://www.omdbapi.com/?apikey={}&{}={}".format(APPID,param,movie)
                x = requests.get(url)
                results = json.loads(x.text)
                movielist.append(results)

        return render_template("favorites.html", movieID=movielist)

@app.route('/translate', methods=['POST'])
def favorites():
        """if query params are passed, write movie to json file."""
        filename = os.path.join('data.json')
        with open(filename) as data_file:
                data = json.load(data_file)
                
        newfavorite = request.form['text']
        data["favorites"].append(newfavorite)
        with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
        return data

@app.route('/search', methods=['POST'])
def search():
        """if POST, query movie api for data and return results."""
        searchtype = 'search'
        query = request.form["title"]
        APPID = os.environ.get('OMDB_API_KEY')
        if searchtype == 'search': param = 's'
        url = "http://www.omdbapi.com/?apikey={}&{}={}".format(APPID,param,query)
        x = requests.get(url)
        results = json.loads(x.text)
        results = results["Search"]
        return render_template('search_results.html', title=query, searchResults=results) 

@app.route('/movie/<movie_imdbID>')
def movie_detail(movie_imdbID):
        """if fetch data from movie database by oid and display info."""
        param = 'i'
        query = movie_imdbID
        APPID = os.environ.get('OMDB_API_KEY')
        url = "http://www.omdbapi.com/?apikey={}&{}={}".format(APPID,param,query)
        x = requests.get(url)
        results = json.loads(x.text)
        title = results['Title']
        return render_template('movie.html', title=title, movieSelect=results)