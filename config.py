"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv
# from secrets import *

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask config variables."""
    FLASK_ENV = 'development'
    TESTING = False
    SECRET_KEY = '?\x84D\x0c\xb6%\xd5\xf7\r\xd6|L\xb7\xfa\xd1\t'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_APP = 'wsgi.py' #environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False