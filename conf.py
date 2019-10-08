import json

class Conf:
        def __init__(self):
            # load and store configuration and update object dictionary
            conf = json.loads("config.json")
            self.__dict__.update(conf)
        
        def __getitem__(self, k):
            # return value of supplied key
            return self.__dict__.get(k, None)