# project/server/user/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user

from project.server import bcrypt, db
from project.server.models import User, Trip, Itinerary
from project.server.user.forms import LoginForm, RegisterForm, TripForm


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)



################
#### routes ####
################

'''
User
'''
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

'''
Trip
'''
@user_blueprint.route('/newtrip', methods=['GET','POST'])
@login_required
def newtrip():
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
            name = form.name.data
        )
        db.session.add(trip)
        db.session.add(itinerary)
        db.session.commit()
        return redirect(url_for("user.trips"))
    return render_template('user/newtrip.html', form=form)

@user_blueprint.route('/trips')
@login_required
def trips():
    all_trips = Trip.query.filter(Trip.users.contains(current_user)).all()
    url = url_for("user.newtrip")
    return render_template('user/trips.html', all_trips= all_trips, url = url)

@user_blueprint.route('/trips/<trip_id>')
@login_required
def specific_trip(trip_id):
    #trip_name = request.args['trip_name']
    trip_id = request.args.get('trip_id')
    trip = Trip.query.filter_by(id=trip_id)
    #query to find all friends in this specific trip
    #users_involved = Trip.query.filter_by(name=message).all()
    return render_template('user/specific_trip.html', trip=trip)

'''
Itinerary
'''
@user_blueprint.route('/trip/<trip_id>/itinerary/<user_id>')
@login_required
def itinerary(trip_id, user_id):

    return render_template('user/itinerary.html', trip=trip)


@user_blueprint.route('/calex')
@login_required
def calex():
    return render_template('user/calex.html')
