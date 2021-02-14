import datetime
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from forecastingchallenge import db
from forecastingchallenge.models import Forecast
from forecastingchallenge.forecasts.forms import ForecastForm

forecasts = Blueprint('forecasts', __name__)


@forecasts.route('/forecast/new', methods=['GET', 'POST'])
@login_required
def forecast_new():
    date = datetime.date.today()  # need to update
    form = ForecastForm()
    if form.validate_on_submit():
        forecast = Forecast(author=current_user, date_predicting=date, location='ZZZZ',
                            temperature_low=form.temperature_low,
                            temperature_high=form.temperature_high,
                            wind_max=form.wind_max,
                            precipitation_chance=form.precipitation_chance,
                            precipitation_amount_low=form.precipitation_amount_low,
                            precipitation_amount_high=form.precipitation_amount_high,
                            precipitation_chance_liquid=form.precipitation_chance_liquid,
                            precipitation_chance_winter=form.precipitation_chance_winter)
        db.session.add(forecast)
        db.session.commit()
        flash('Forecast successfully submitted', 'success')
        return redirect(url_for('main.home'))
    return render_template('forecast_new.html', form=form)
