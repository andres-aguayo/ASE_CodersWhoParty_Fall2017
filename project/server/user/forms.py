# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40)
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

class TripForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    location = StringField('Location', [DataRequired()])
    start_date = DateField('Start Date', [DataRequired()],description='MM/DD/YYYY',format='%m/%d/%Y')
    end_date = DateField('End Date', [DataRequired()],description='MM/DD/YYYY',format='%m/%d/%Y')

class EventsForm(FlaskForm):
    name = StringField('Name of Event', [DataRequired()])
    description = StringField('Description of Event')
    start_date = DateField('Start Date', [DataRequired()],description='MM/DD/YYYY',format='%m/%d/%Y')
    start_time = DateTimeField('Start Time', [DataRequired()],description='HH:MM',format='%H:%M')
    end_date = DateField('End Date', [DataRequired()],description='MM/DD/YYYY',format='%m/%d/%Y')
    end_time = DateTimeField('End Time', [DataRequired()],description='HH:MM',format='%H:%M')

class UserForm(FlaskForm):
    user = StringField('User', [DataRequired(), Email()])
