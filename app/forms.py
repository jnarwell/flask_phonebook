from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, EqualTo

class PhonebookForm(FlaskForm):
    first = StringField('First Name', validators=[InputRequired()])
    last = StringField('Last Name', validators=[InputRequired()])
    phone = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    submit = SubmitField('Add Contact')