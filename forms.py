from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

categories = [("recommended","Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")]

## Create Form Here
class AddLocationForm(FlaskForm):
  name = StringField("Location Name",validators=[DataRequired()])
  description = TextAreaField("Location Description",validators=[DataRequired()])
  category = RadioField("Category",choices=categories)
  submit = SubmitField("Add Location")
