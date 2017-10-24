# project/server/models.py


import datetime

from project.server import app, db, bcrypt

'''
helper table for many-to-many relationship b/w User and Trip
'''
users_trips = db.Table('users_trips',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('trip_id',db.Integer, db.ForeignKey('trip.id'), primary_key=True)
)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    trips = db.relationship('Trip', secondary=users_trips, lazy='subquery', backref=db.backref('users', lazy=True))

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
    users = db.relationship('User', secondary=users_trips, lazy='subquery', backref=db.backref('trips', lazy=True))

    def __init__(self, name, location, start_date, end_date, users, itineraries):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.users = users
        #self.itineraries = itineraries

    def __repr__(self):
        return '<Trip {0}'.format(self.name)

