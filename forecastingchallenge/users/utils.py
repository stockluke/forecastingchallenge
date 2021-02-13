import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from forecastingchallenge import app, mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)
    ################################# need to account for aspect ratio
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename


def delete_picture(picture_filename):
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)
    try:
        os.remove(picture_path)
    except OSError:
        pass


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='forecastingchallenge@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
{url_for('users.reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
