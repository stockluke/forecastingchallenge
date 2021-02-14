from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class ForecastForm(FlaskForm):
    temperature_low = IntegerField('Low Temperature (°F)',
                                   validators=[DataRequired(), NumberRange(min=-128, max=135)])
    temperature_high = IntegerField('High Temperature (°F)',
                                    validators=[DataRequired(), NumberRange(min=-128, max=135)])
    wind_max = IntegerField('Max Wind Speed (knots)',
                            validators=[DataRequired(), NumberRange(min=0, max=200)])
    precipitation_chance = DecimalField('Precipitation Chance (0-1)',
                                        validators=[DataRequired(), NumberRange(min=0, max=1)])
    precipitation_amount_low = DecimalField('Low Precipitation Amount (inches)',
                                            validators=[DataRequired(), NumberRange(min=0, max=72)])
    precipitation_amount_high = DecimalField('High Precipitation Amount (inches)',
                                             validators=[DataRequired(), NumberRange(min=0, max=72)])
    precipitation_chance_liquid = DecimalField('Precipitation Liquid Chance (0-1)',
                                               validators=[DataRequired(), NumberRange(min=0, max=1)])
    precipitation_chance_winter = DecimalField('Precipitation Winter Chance (0-1)',
                                               validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Submit')

    def validate_temperature_low(self, temperature_low):
        if temperature_low.data > self.temperature_high.data:
            raise ValidationError('Your low temperature is greater than your high temperature.')

    def validate_temperature_high(self, temperature_high):
        if self.temperature_low.data > temperature_high.data:
            raise ValidationError('Did you get your temperatures backwards?')

    def validate_precipitation_amount_low(self, precipitation_amount_low):
        if precipitation_amount_low.data > self.precipitation_amount_high.data:
            raise ValidationError('Your low precipitation is greater than your high precipitation.')

    def validate_precipitation_amount_high(self, precipitation_amount_high):
        if self.precipitation_amount_low.data > precipitation_amount_high.data:
            raise ValidationError('Did you get your precipitation amounts backwards?')
