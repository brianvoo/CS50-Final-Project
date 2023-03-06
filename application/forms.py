from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, email_validator, Email, EqualTo
from flask import Blueprint

forms_bp = Blueprint(
    'forms_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=("Please input a valid email address."))
        ]
    )
    body = StringField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
            message=("Your message is too short."))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    """Signup Form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            DataRequired(),
            Email(message=("Please input a valid email address."))
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(),
            Length(min=4, message=("Selected a stronger password."))
        ]
    )
    confirm = PasswordField(
        'Confirm your Password',
        [
            DataRequired(),
            EqualTo('password', message=("Passwords must match."))
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """Login form."""
    email = StringField(
        'Email',
        [
            DataRequired(),
            Email(message=("Please input a valid email address."))
        ]
    )
    password = PasswordField(
        [
            DataRequired(),
        ]
    )
    submit = SubmitField('Login')