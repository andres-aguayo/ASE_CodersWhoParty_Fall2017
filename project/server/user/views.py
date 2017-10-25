# project/server/user/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user

from project.server import bcrypt, db
from project.server.models import User, Trip
from project.server.user.forms import LoginForm, RegisterForm, TripForm


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)



################
#### routes ####
################

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

@user_blueprint.route('/newtrip', methods = ['GET','POST'])
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
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for("user.trips"))
    return render_template('user/newtrip.html', form=form)

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


@user_blueprint.route('/trips')
@login_required
def trips():
    helper = current_user
    all_trips = Trip.query.filter(Trip.users.contains(helper)).all()
    return render_template('user/trips.html', all_trips= all_trips)


@user_blueprint.route('/calex')
@login_required
def calex():
    return render_template('user/calex.html')
