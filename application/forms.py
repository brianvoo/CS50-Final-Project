from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, email_validator, Email
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