from flask import render_template, flash, redirect
from app import app
from app.forms import TopCities


@app.route("/", methods=['GET', 'POST'])
def home():
    name = 'Thuy Tran'
    title = 'Top Cities'
    form = TopCities()
    top_cities = [{'city':'Paris'},\
                  {'city':'London'},\
                  {'city':'Rome'},\
                  {'city': 'Tahiti'} ]
    if form.validate_on_submit():
        flash('submited!')
        return redirect('/')
    return render_template("home.html", form=form, name=name, title=title, top_cities=top_cities)
