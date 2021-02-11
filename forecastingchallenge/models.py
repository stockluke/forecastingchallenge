from datetime import datetime
from forecastingchallenge import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    forecasts = db.relationship('Forecast', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(4), nullable=False)
    date_effective = db.Column(db.DateTime, nullable=False)
    #forecasts = db.relationship('Forecast', backref='location', lazy=True)

    def __repr__(self):
        return f"Post('{self.location}', '{self.date_effective}')"


class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_predicting = db.Column(db.DateTime, nullable=False)
    #location = db.Column(db.String(4), db.ForeignKey('location.id'), nullable=False)
    temperature_high = db.Column(db.Integer, nullable=False)
    temperature_low = db.Column(db.Integer, nullable=False)
    wind_max = db.Column(db.Integer, nullable=False)
    precipitation_amount = db.Column(db.Float, nullable=False)
    precipitation_chance = db.Column(db.Float, nullable=False)
    precipitation_chance_liquid = db.Column(db.Boolean, nullable=False)
    precipitation_chance_winter = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Forecast('{self.user_id}', '{self.location}', '{self.date_posted}', '{self.date_predicting}')"
