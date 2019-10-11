from app import app
import sys
import math
import os
from flask import Flask, escape, request, render_template, flash
import json
import requests
from requests.exceptions import HTTPError
from flask_bootstrap import Bootstrap
#from conf import Config, Conf, Favs
import conf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

@app.route('/')
def index():
        user = {'username': 'Arthur'}
        return render_template('index.html', title='Home', user=user)
        

@app.route('/favorites')
def readfavorites():
    #Read out favorited movies.
    filename = os.path.join("data.json")
    with open(filename) as data_file:
        fav_list = json.load(data_file)
        fav_list = fav_list["favorites"]

    with open("config.json") as datafile:
            data = json.load(datafile)
            appid = data["omdb_api_key"]
    param = "i"
    movielist = []
    for movie in fav_list:
        #print("movie: ", movie)
        url = "http://www.omdbapi.com/?apikey={}&{}={}".format(appid,param,movie)
        x = requests.get(url)
        results = json.loads(x.text)
        movielist.append(results)

    #print("List: ", movielist)
    return render_template("favorites.html", movieID=movielist)

@app.route('/translate', methods=['POST'])
def favorites():
    """if query params are passed, write movie to json file."""
#     print("Here")
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
        
    newfavorite = request.form['text']
    #print(data['favorites'])
    data["favorites"].append(newfavorite)
    #print(data['favorites'])
    with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    return data

@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    # include some validation on the search input
    searchtype = 'search'
    query = request.form["title"]
    with open('config.json') as datafile:
            data = json.load(datafile)
            appid = data["omdb_api_key"]
            #print(appid)
    #print("Query: ",query)
    if searchtype == 'search': param = 's'
    url = "http://www.omdbapi.com/?apikey={}&{}={}".format(appid,param,query)
    x = requests.get(url)
    results = json.loads(x.text)
    results = results["Search"]
    #print(type(results))
    
    return render_template('search_results.html', title=query, searchResults=results) 

@app.route('/movie/<movie_imdbID>')
def movie_detail(movie_imdbID):
    """if fetch data from movie database by oid and display info."""
    param = 'i'
    query = movie_imdbID
    #print("IMDB ID: ",query)
    url = "http://www.omdbapi.com/?apikey=815bb1ac&{}={}".format(param,query)
    x = requests.get(url)
    results = json.loads(x.text)
    title = results['Title']
    #print('Results: ', results)
    return render_template('movie.html', title=title, movieSelect=results)