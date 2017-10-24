# project/server/trip/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask_login import login_user, logout_user, login_required

from project.server import bcrypt, db
from project.server.models import Trip
from project.server.trip.forms import NewTripForm

################
#### config ####
################

trip_blueprint = Blueprint('trip', __name__,)


################
#### routes ####
################

@trip_blueprint.route('/new_trip', methods=['GET', 'POST'])
@login_required
def new_trip():
    form = NewTripForm(request.form)
    if form.validate_on_submit():
        trip = Trip(
            name=form.name.data,
            location=form.location.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data
        )
        db.session.add(form)
        db.session.commit()


        flash('New trip {} created.'.format(form.name.data), 'success')
        return redirect(url_for("main.home"))

    return render_template('user/new_trip.html', form=form)


