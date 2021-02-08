from flask import render_template, url_for, flash, redirect
from forecastingchallenge import app
from forecastingchallenge.forms import RegistrationForm, LoginForm
from forecastingchallenge.models import User, Post


posts = [
    {
        'key1': 'data1',
        'key2': 'data2',
        'key3': 'data3',
        'key4': 'data4'
    },
    {
        'key1': 'data5',
        'key2': 'data6',
        'key3': 'data7',
        'key4': 'data8'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)
