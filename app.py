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
from app.models import User, Favorites






