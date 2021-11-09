from app import db


class City(db.Model):
    # create the columns:
    # rank(int, unique, index)
    # name(String, unique, index)
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(120), unique=True, index=True)
    city_rank = db.Column(db.Integer, unique=True, index=True)

    # function to check for the city_rank
    def check_rank(self, city_rank):
        # check if the rank of the city exits in database
        # return True for yes and False for not
        if city_rank != self.city_rank:
            return False
        return True
    
    # function to check for the city_name
    def check_city(self, city_name):
        # check if the name of the city exits in database
        # return True for yes and False for not
        if city_name != self.city_name:
            return False
        return True

    def __init__(self, city_name, city_rank):
        self.city_name = city_name
        self.city_rank = city_rank

    def __repr__(self):
        return f'<City {self.city_name} : {self.city_rank}>'

# class CityRank(db.Model):
   # __tablename__ = 'city_rank'
    #id = db.Column(db.Integer, primary_key=True)
    #city_rank = db.Column(db.Integer, unique=False, nullable=False)
    #city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    # def __repr__(self):
        # return f'<Rank {self.rank}>'


db.create_all()
db.session.commit()
