from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField, RadioField, StringField, SubmitField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired


class PurchaseForm(FlaskForm):
    id = IntegerField(default=0, widget=HiddenInput())
    from_currency = StringField('From coin', validators=[DataRequired(message="Please, add origin coin")])
    from_quantity = FloatField('Quantity', validators=[DataRequired(message="Please, add the quantity")])
    to_currency = StringField('To coin', validators=[DataRequired(message="Please, add the final coin")])
    submit = SubmitField('purchase')