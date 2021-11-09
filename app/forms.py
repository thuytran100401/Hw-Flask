from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    # add form for the TopCities
    # city_name (String) validator should make the data and textbox required
    # city_rank (Integer) validator should make the data and textbox required
    # is_visited (Boolean) checkbox for True or False
    # submit (button ) text should say 'Submit'
    city_name = StringField('City Name', validators=[DataRequired()])
    city_rank = IntegerField('City Rank', validators=[DataRequired()])
    is_visited = BooleanField('Visited')
    submit = SubmitField('Submit')