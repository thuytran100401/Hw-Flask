from flask import render_template, flash, redirect
from app import app
from app.forms import TopCities
from app import db
from app.models import City
from operator import itemgetter

# add route '/' and add two methods to handle request
# by the user: 'GET' and 'POST'
@app.route("/", methods=['GET', 'POST'])
def home():
    # create a variable of name
    name = 'Thuy Tran'
    
    # create a variable of title
    title = 'Top Cities'
    
    # create a form from the TopCities classd
    form = TopCities()
    
    # create a list of city with the city and its rank from database
    cityList = City.query.all()
    top_cities = [
            
    ]
    
    # add the item from the database to the top_cities list
    for i in cityList:
        top_cities.append({'city': i.city_name, 'rank': i.city_rank}) 
    
    # function to get the rank of the city   
    def get_rank(top_cities):
        return top_cities.get('rank')
    
    # sort the top_cities list by the rank of the city
    top_cities.sort(key=get_rank) 
           
    if form.validate_on_submit():
        # if the form submit then check if the city is exited in the database
        # if not create the city and add to database
        city = City.query.filter_by(city_name=form.city_name.data).first()
        rank = City.query.filter_by(city_rank=form.city_rank.data).first()
        if city is None or not city.check_city(form.city_name.data):
            # check if the rank of the city is exist
            if rank is None or not rank.check_rank(form.city_rank.data):
                city_name = form.city_name.data
                city_rank = form.city_rank.data
                # add the city name and its rank to database
                city = City(city_name,city_rank)
                db.session.add(city)
                db.session.commit()
                flash(f'{form.city_name.data} is submited and added, is_visited = {form.is_visited.data}!')
                return redirect('/')
            else:
                flash(f'Rank #{form.city_rank.data} is already exist with other city!')
                return redirect('/')        
        else:
            flash(f'{form.city_name.data} is already exist!')  
            return redirect('/') 
         
    return render_template("home.html", form=form, name=name, title=title, top_cities=top_cities)
