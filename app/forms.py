from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    city_name = StringField('City Name', validator=[DataRequired])
    city_rank = IntegerField('City Rank', validator=[DataRequired])
    is_visited = BooleanField('Visited')
    submit = SubmitField('Submit')