# project/server/user/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user

from project.server import bcrypt, db
from project.server.models import User, Trip, Itinerary, Event
from project.server.user.forms import LoginForm, RegisterForm, TripForm, EventsForm, UserForm


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

##########
## User ##
##########

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash('Thank you for registering.', 'success')
        return redirect(url_for("user.trips"))

    return render_template('user/register.html', form=form)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('user.trips'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', title='Please Login', form=form)

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.home'))


##########
## Trip ##
##########

'''
need to implement empty functions

otherwise trip functionality looking all right
'''

@user_blueprint.route('/new_trip', methods=['GET','POST'])
@login_required
def new_trip():
    form= TripForm(request.form)
    if form.validate_on_submit():
        trip = Trip(
            name = form.name.data,
            location = form.location.data,
            start_date = form.start_date.data,
            end_date = form.end_date.data,
            user = current_user
        )
        itinerary = Itinerary(
            name = form.name.data,
            trip = trip,
            user = current_user
        )
        db.session.add(trip)
        db.session.add(itinerary)
        db.session.commit()
        return redirect(url_for("user.trips"))
    return render_template('user/new_trip.html', form=form)

@user_blueprint.route('/trips')
@login_required
def trips():
    all_trips = Trip.query.filter(Trip.users.contains(current_user)).all()
    return render_template('user/trips.html', all_trips= all_trips)

@user_blueprint.route('/trips/<trip_id>', methods=['GET', 'POST'])
@login_required
def specific_trip(trip_id):
    # looks for trip, if its not there, then 404s
    trip = Trip.query.filter_by(id=trip_id).first_or_404()
    users = User.query.filter(User.trips.contains(trip)).all()
    users.remove(current_user)
    form = UserForm(request.form)
    if form.validate_on_submit():
        user1 = User.query.filter_by(email=form.user.data).first()
        if user1:
            itinerary = Itinerary(
                name = trip.name,
                trip = trip,
                user = user1
            )
            trip.users.append(user1)
            db.session.add(trip)
            db.session.add(itinerary)
            db.session.commit()
            users = User.query.filter(User.trips.contains(trip)).all()
            users.remove(current_user)
        else:
            flash('There is no user with this email address.', 'danger')
    return render_template('user/specific_trip.html', trip=trip, users=users, current_user=current_user, form=form)

# IMPLEMENT ME
def delete_trip():
    pass

# IMPLEMENT ME
'''
whats the functionality here besides changing basic trip info?
should we be able to remove users from trip?
'''
def edit_trip():
    pass


###############
## Itinerary ##
###############

'''
thoughts for thots

should a user be able to delete their itinerary?
or should they just be able to leave a trip and auto-delete itinerary?

how should editing an itinerary work?
is that really just editing the events of an itinerary?
'''

@user_blueprint.route('/trips/<trip_id>/itinerary/<user_id>')
@login_required
def itinerary(trip_id, user_id):
    # query database for relevant info
    trip = Trip.query.filter_by(id=trip_id).first_or_404()
    user = User.query.filter_by(id=user_id).first_or_404()
    itinerary = Itinerary.query.filter_by(trip=trip, user=user).first_or_404()
    events = itinerary.events

    # check if user is current user for dynamic web page
    is_current_user = False
    if user == current_user:
        is_current_user = True

    return render_template('user/itinerary.html', trip=trip, user=user, events=events, is_current_user=is_current_user, itinerary = itinerary)

###########
## EVENT ##
###########

'''
this shit below needs to be implemented
'''

# IMPLEMENT ME
def event():
    pass

# IMPLEMENT ME
@user_blueprint.route('/new_event/<itinerary>', methods=['GET','POST'])
@login_required
def new_event(itinerary):
    form= EventsForm(request.form)
    if form.validate_on_submit():
        itinerary = Itinerary.query.filter_by(id=itinerary).first_or_404()
        start_date = form.start_date.data
        end_date = form.end_date.data
        event = Event(
            name = form.name.data,
            description = form.description.data,
            start_time = form.start_time.data.replace(year=start_date.year, month=start_date.month, day=start_date.day),
            end_time = form.end_time.data.replace(year=end_date.year, month=end_date.month, day=end_date.day),
            itinerary = itinerary
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("user.itinerary" , trip_id=itinerary.trip.id, user_id=itinerary.user.id))
    return render_template('user/new_event.html', form=form)

# IMPLEMENT ME
def edit_event():
    pass

# IMPLEMENT ME
'''
should only be able to be deleted by person who created event?
or should an event be deleted once everyone deletes it?
why not both?
'''
def delete_event():
    pass

# what are we doing with this?
@user_blueprint.route('/calex')
@login_required
def calex():
    return render_template('user/calex.html')
