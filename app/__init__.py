import flask 
import os
from flask_sqlalchemy import SQLAlchemy

# the location, directory of the the database file
basedir = os.path.abspath(os.path.dirname(__file__))

# instance of the Flask class
app = flask.Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'haha',
    # where to locate the database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

from app import routes, models