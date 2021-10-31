from os import name
from app import myapp
from app.forms import TopCities
from flask import render_template, flask, redirect

# instance of the Flask class
myapp = flask.Flask(__name__)

myapp.config.from_mapping(
    SECRET_KEY = 'it-dont-matter'
)

@myapp.route("/", methods=['GET', 'POST'])
def home():
    form = TopCities()
    if form.validate_on_submit():
        flask(f'{form.city_name.data} is submitted at rank {form.city_rank.data}, is_visited={form.is_visited.data}')
        return redirect('/')
    title = 'Top Cities'
    name = 'Thuy Tran'
    return render_template('home.html', form=form, name=name, title=title)

