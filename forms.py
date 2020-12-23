from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = SelectField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    
    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')