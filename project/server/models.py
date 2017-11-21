# project/server/models.py


import datetime

from project.server import app, db, bcrypt


#helper table for many-to-many relationship b/w User and Trip
users_trips = db.Table('users_trips', db.Model.metadata,
    db.Column('user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('trip',db.Integer, db.ForeignKey('trips.id'), primary_key=True)
)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    trips = db.relationship("Trip", secondary= users_trips, back_populates = "users")
    itineraries = db.relationship("Itinerary", back_populates="user")

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode('utf-8')
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)

class Trip(db.Model):

    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    # we should add date constraitns: start_date < end_date
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    users = db.relationship("User", secondary = users_trips, back_populates= "trips")
    itineraries = db.relationship("Itinerary", back_populates="trip")

    def __init__(self, name, location, start_date, end_date, user):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.users.append(user)

    def __repr__(self):
        return '<Trip {0}'.format(self.name)

class Itinerary(db.Model):

    __tablename__ = "itineraries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    events = db.relationship("Event",back_populates="itinerary")
    trip = db.relationship("Trip", back_populates="itineraries")
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"))
    user = db.relationship("User", back_populates="itineraries")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def __init__(self, name, trip, user):
        self.name = name
        self.trip = trip
        self.user = user

class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))
    itinerary = db.relationship("Itinerary", back_populates="events")
