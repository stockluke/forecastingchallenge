from flask import render_template, url_for, flash, redirect, request
from forecastingchallenge import app, db, bcrypt
from forecastingchallenge.forms import RegistrationForm, LoginForm, UpdateAccountForm
from forecastingchallenge.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        valid_password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and valid_password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout successful','success')
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', form=form, image_file=image_file)