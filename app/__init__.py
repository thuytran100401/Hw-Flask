
import flask

# instance of the Flask class
app = flask.Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'it-dont-matter'
)

from app import routes