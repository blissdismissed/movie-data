import json
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Conf:
        def __init__(self):
            # load and store configuration and update object dictionary
            with open('config.json') as j:
                conf = json.load(j)
            self.__dict__.update(conf)
        
        def __getitem__(self, k):
            # return value of supplied key
            return self.__dict__.get(k, None)

class Favs:
        def __init__(self):
            # load and store configuration and update object dictionary
            with open('data.json') as d:
                fav_data = json.load(d)
            self.__dict__.update(fav_data)
        
        def __getitem__(self, m):
            # return value of supplied key
            return self.__dict__.get(m, None)


class Config(object):
    # configuration for backend
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

