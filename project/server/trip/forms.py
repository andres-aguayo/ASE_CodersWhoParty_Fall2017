# project/server/trip/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired

class NewTripForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    location = StringField('Location', [DataRequired()])
    start_date = DateField('Start date', [DataRequired()])
    end_date =  DateField('End date', [DataRequired()])

