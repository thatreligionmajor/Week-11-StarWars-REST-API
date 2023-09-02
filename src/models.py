from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#db.Model = declarative_db.Model()

# class User(db.Model):
#     __tablename__ = 'user'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     email = Column(String(250), nullable=False)
#     username = Column(String(30), nullable=False)
#     password = Column(String(30), nullable=False)

#     def serialize(self):
#         return{
#             "email": self.email,
#             "username": self.username,
#         }

class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String(30), nullable=False)
    rotation_period = db.Column(db.String(30), nullable=False)
    orbital_period = db.Column(db.String(30), nullable=False)
    gravity = db.Column(db.String(30), nullable=False)
    population = db.Column(db.String(30), nullable=False)
    climate = db.Column(db.String(30), nullable=False)
    terrain = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String(30), nullable=True)
    
    def serialize(self):
        return{
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "description": self.description
        }
    
class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    vehicle_class = db.Column(db.String(50), nullable=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    cost_in_credits = db.Column(db.String(50), nullable=True)
    length = db.Column(db.String(50), nullable=True)
    crew = db.Column(db.String(50), nullable=True)
    passengers = db.Column(db.String(50), nullable=True)
    
    def serialize(self):
        return{
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers
        }

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    persons_name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=True)
    mass = db.Column(db.String(50), nullable=True)
    hair_color = db.Column(db.String(50), nullable=True)
    skin_color = db.Column(db.String(50), nullable=True)
    eye_color = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    # planet_id = db.Column(db.Integer, ForeignKey('planets.id'))
    # vehicle_id = db.Column(db.Integer, ForeignKey('vehicles.id'))
    # planet = relationship(Planets)
    # vehicle = relationship(Vehicles)
    
    def serialize(self):
        return{
            "persons_name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            # "planet_id": self.planet_id,
            # "vehicle_id": self.vehicle_id
        }
    
# class Favorites(db.Model):
#     __tablename__ = "favorites"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     person_id = Column(Integer, ForeignKey('people.id'), nullable=True)
#     planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
#     vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)

#     user = relationship(User)
#     people = relationship(people)
#     planets = relationship(Planets)
#     vehicles = relationship(Vehicles)
    

#     def serialize(self):
#         return{
#             "user_id": self.user_id,
#             "person_id": self.person_id,
#             "planet_id": self.planet_id,
#             "vehicle_id": self.vehicle_id
#         }
    
## Draw from SQLAlchemy db.Model
# render_er(db.Model, 'diagram.png')